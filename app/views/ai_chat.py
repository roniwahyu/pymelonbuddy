import streamlit as st
from app.services.gemini_service import GeminiService
from app.services.openrouter_service import OpenRouterService
import config

def show():
    st.title("AI Consultation 🤖")
    
    # Model selection
    ai_model = st.sidebar.selectbox(
        "Select AI Model",
        ["Gemini", "OpenRouter - Claude", "OpenRouter - GPT-4"],
        index=0
    )
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about your melon cultivation..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get AI response based on selected model
        with st.spinner("Thinking..."):
            if ai_model == "Gemini":
                service = GeminiService()
                response = service.get_response(prompt)
            else:
                service = OpenRouterService()
                model = "anthropic/claude-3-opus" if "Claude" in ai_model else "openai/gpt-4"
                response = service.get_response(prompt, model=model)
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Option to upload an image for analysis
    st.sidebar.markdown("---")
    st.sidebar.subheader("Image Analysis")
    uploaded_file = st.sidebar.file_uploader("Upload a leaf or plant image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.sidebar.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        if st.sidebar.button("Analyze Image"):
            with st.spinner("Analyzing image..."):
                # Here we would integrate with the image analysis service
                st.sidebar.success("Analysis complete! See results in chat.")
                
                # Add a placeholder response - in a real app, this would come from the AI
                analysis_result = """
                **Plant Analysis Results:**
                
                - **Health Status**: Good overall condition
                - **Potential Issues**: Slight signs of nutrient deficiency (magnesium)
                - **Recommendations**: 
                  1. Adjust nutrient solution to increase magnesium levels
                  2. Monitor EC levels more frequently
                  3. Consider adjusting pH to 5.8-6.2 range
                """
                
                # Add to chat
                with st.chat_message("assistant"):
                    st.markdown(analysis_result)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": analysis_result})