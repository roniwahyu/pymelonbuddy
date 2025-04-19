import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import random  # For demo data, remove in production
import io
from PIL import Image
import numpy as np

def show():
    st.title("Plant Analysis & Diagnostics 🔍")
    
    # Create tabs for different analysis sections
    tab1, tab2, tab3 = st.tabs(["Leaf Analysis", "Disease Detection", "Growth Prediction"])
    
    with tab1:
        leaf_analysis()
    
    with tab2:
        disease_detection()
    
    with tab3:
        growth_prediction()

def leaf_analysis():
    st.subheader("Leaf Analysis")
    
    # Upload image section
    st.write("#### Upload Leaf Image")
    
    uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Leaf Image", use_column_width=True)
        
        # Analysis options
        st.write("#### Analysis Options")
        
        analysis_type = st.multiselect(
            "Select Analysis Types",
            ["Nutrient Deficiency", "Disease Detection", "Chlorophyll Content", "Leaf Area"],
            default=["Nutrient Deficiency", "Chlorophyll Content"]
        )
        
        ai_model = st.selectbox(
            "Select AI Model",
            ["Gemini Pro Vision", "OpenRouter - Claude Vision", "OpenRouter - GPT-4 Vision"]
        )
        
        # Analyze button
        if st.button("Analyze Leaf"):
            with st.spinner("Analyzing leaf image..."):
                # Simulate processing time
                import time
                time.sleep(2)
                
                # Display analysis results (in a real app, this would come from the AI model)
                st.success("Analysis complete!")
                
                st.write("#### Analysis Results")
                
                # Nutrient status results
                if "Nutrient Deficiency" in analysis_type:
                    st.write("**Nutrient Status:**")
                    
                    # Create demo data for nutrient levels
                    nutrients = {
                        "Nitrogen": {"value": 85, "status": "Optimal", "color": "green"},
                        "Phosphorus": {"value": 65, "status": "Adequate", "color": "green"},
                        "Potassium": {"value": 90, "status": "Optimal", "color": "green"},
                        "Calcium": {"value": 45, "status": "Deficient", "color": "red"},
                        "Magnesium": {"value": 60, "status": "Low", "color": "orange"},
                        "Iron": {"value": 75, "status": "Adequate", "color": "green"}
                    }
                    
                    # Create gauge charts for each nutrient
                    for nutrient, data in nutrients.items():
                        fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=data["value"],
                            title={"text": f"{nutrient} ({data['status']})"},
                            gauge={
                                "axis": {"range": [0, 100]},
                                "bar": {"color": data["color"]},
                                "steps": [
                                    {"range": [0, 40], "color": "red"},
                                    {"range": [40, 70], "color": "orange"},
                                    {"range": [70, 100], "color": "green"}
                                ]
                            }
                        ))
                        
                        fig.update_layout(height=200)
                        st.plotly_chart(fig, use_container_width=True)
                
                # Chlorophyll content
                if "Chlorophyll Content" in analysis_type:
                    st.write("**Chlorophyll Content Analysis:**")
                    
                    # Create a heatmap visualization of the leaf
                    # In a real app, this would be generated from image processing
                    chlorophyll_data = np.random.normal(0.7, 0.2, (50, 50))
                    chlorophyll_data = np.clip(chlorophyll_data, 0, 1)
                    
                    fig = px.imshow(
                        chlorophyll_data,
                        color_continuous_scale="Viridis",
                        title="Chlorophyll Distribution Map"
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    avg_chlorophyll = np.mean(chlorophyll_data)
                    st.metric(
                        label="Average Chlorophyll Content",
                        value=f"{avg_chlorophyll:.2f}",
                        delta=f"{(avg_chlorophyll - 0.65) * 100:.1f}% vs. healthy reference"
                    )
                
                # Leaf area
                if "Leaf Area" in analysis_type:
                    st.write("**Leaf Area Analysis:**")
                    
                    # Demo leaf area calculation
                    leaf_area = random.uniform(80, 120)
                    avg_area = 100
                    
                    st.metric(
                        label="Leaf Area",
                        value=f"{leaf_area:.1f} cm²",
                        delta=f"{(leaf_area - avg_area) / avg_area * 100:.1f}% vs. average"
                    )
                
                # AI recommendations
                st.write("**AI Recommendations:**")
                
                recommendations = """
                Based on the leaf analysis, I recommend the following actions:
                
                1. **Calcium Deficiency Treatment**: Apply a calcium-rich foliar spray (e.g., calcium nitrate solution at 2-3g/L) twice weekly until symptoms improve.
                
                2. **Magnesium Supplementation**: Add Epsom salts (magnesium sulfate) at 1g/L to your nutrient solution to address the low magnesium levels.
                
                3. **Monitoring**: Re-analyze in 7 days to check if nutrient levels are improving.
                
                4. **Preventive Measures**: Ensure pH is maintained between 5.8-6.2 to optimize calcium and magnesium uptake.
                
                The overall plant health appears good, with adequate levels of nitrogen, phosphorus, and potassium. The chlorophyll content is slightly above average, indicating good photosynthetic capacity.
                """
                
                st.markdown(recommendations)

def disease_detection():
    st.subheader("Disease Detection")
    
    # Upload image section
    st.write("#### Upload Plant Image")
    
    uploaded_file = st.file_uploader("Choose a plant image...", type=["jpg", "jpeg", "png"], key="disease_uploader")
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Plant Image", use_column_width=True)
        
        # Analysis options
        st.write("#### Detection Options")
        
        detection_sensitivity = st.slider("Detection Sensitivity", 0.0, 1.0, 0.7, 0.1)
        
        ai_model = st.selectbox(
            "Select AI Model",
            ["Gemini Pro Vision", "OpenRouter - Claude Vision", "OpenRouter - GPT-4 Vision"],
            key="disease_model"
        )
        
        # Detect button
        if st.button("Detect Diseases"):
            with st.spinner("Analyzing image for diseases..."):
                # Simulate processing time
                import time
                time.sleep(2)
                
                # Display detection results (in a real app, this would come from the AI model)
                st.success("Analysis complete!")
                
                st.write("#### Detection Results")
                
                # Demo disease detection results
                diseases = [
                    {"name": "Powdery Mildew", "confidence": 0.82, "severity": "Mild"},
                    {"name": "Leaf Spot", "confidence": 0.35, "severity": "Not Detected"},
                    {"name": "Downy Mildew", "confidence": 0.12, "severity": "Not Detected"},
                    {"name": "Anthracnose", "confidence": 0.08, "severity": "Not Detected"},
                    {"name": "Fusarium Wilt", "confidence": 0.05, "severity": "Not Detected"}
                ]
                
                # Filter based on sensitivity
                detected_diseases = [d for d in diseases if d["confidence"] >= detection_sensitivity]
                
                if detected_diseases:
                    # Create bar chart for confidence levels
                    fig = px.bar(
                        diseases,
                        x="name",
                        y="confidence",
                        color="confidence",
                        color_continuous_scale="Reds",
                        title="Disease Detection Confidence"
                    )
                    
                    fig.update_layout(
                        xaxis_title="Disease",
                        yaxis_title="Confidence Score",
                        yaxis=dict(range=[0, 1])
                    )
                    
                    # Add threshold line
                    fig.add_shape(
                        type="line",
                        x0=-0.5,
                        x1=len(diseases) - 0.5,
                        y0=detection_sensitivity,
                        y1=detection_sensitivity,
                        line=dict(color="black", width=2, dash="dash")
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Display detailed information for detected diseases
                    st.write("**Detected Diseases:**")
                    
                    for disease in detected_diseases:
                        with st.expander(f"{disease['name']} - Confidence: {disease['confidence']:.2f}"):
                            st.write(f"**Severity:** {disease['severity']}")
                            
                            if disease['name'] == "Powdery Mildew":
                                st.write("""
                                **Description:** Powdery mildew appears as white powdery spots on the leaves and stems. 
                                It's caused by fungal pathogens and thrives in humid conditions with moderate temperatures.
                                
                                **Treatment Options:**
                                1. Apply fungicide specifically formulated for powdery mildew
                                2. Increase air circulation around plants
                                3. Avoid overhead watering
                                4. Remove and destroy affected leaves
                                
                                **Prevention:**
                                1. Maintain proper plant spacing
                                2. Use resistant varieties when possible
                                3. Apply preventive fungicides during high-risk periods
                                """)
                else:
                    st.info("No diseases detected with the current sensitivity threshold.")
                
                # AI recommendations
                st.write("**AI Recommendations:**")
                
                if detected_diseases:
                    recommendations = """
                    Based on the disease detection results, I recommend the following actions:
                    
                    1. **Immediate Treatment**: Apply a fungicide specifically formulated for powdery mildew, such as potassium bicarbonate or neem oil solution.
                    
                    2. **Cultural Practices**: Improve air circulation around the plants by proper spacing and pruning. Avoid overhead watering to keep foliage dry.
                    
                    3. **Monitoring**: Check plants daily for disease progression. The current infection is mild and caught early, which improves treatment outcomes.
                    
                    4. **Preventive Measures**: Apply preventive fungicides to unaffected plants, especially during periods of high humidity.
                    
                    5. **Sanitation**: Remove and destroy severely affected leaves to prevent spore spread.
                    """
                else:
                    recommendations = """
                    No diseases were detected with the current sensitivity threshold. However, I recommend the following preventive measures:
                    
                    1. **Regular Monitoring**: Continue to inspect plants regularly for early signs of disease.
                    
                    2. **Preventive Practices**: Maintain good air circulation, avoid overhead watering, and ensure proper plant spacing.
                    
                    3. **Nutrient Management**: Ensure balanced nutrition to strengthen plant immune responses.
                    
                    4. **Environmental Control**: Monitor and maintain optimal temperature and humidity levels in your growing environment.
                    """
                
                st.markdown(recommendations)

def growth_prediction():
    st.subheader("Growth Prediction")
    
    # Plant selection
    st.write("#### Select Plant")
    
    plant = st.selectbox(
        "Plant",
        ["Plant #1 (Honeydew)", "Plant #2 (Cantaloupe)", "Plant #3 (Galia)"]
    )
    
    # Current metrics
    st.write("#### Current Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        current_height = st.number_input("Current Height (cm)", min_value=0.0, value=25.0, step=0.5)
    
    with col2:
        current_leaves = st.number_input("Leaf Count", min_value=0, value=12, step=1)
    
    with col3:
        days_since_planting = st.number_input("Days Since Planting", min_value=0, value=25, step=1)
    
    # Environmental factors
    st.write("#### Environmental Factors")
    
    col1, col2 = st.columns(2)
    
    with col1:
        temperature = st.slider("Average Temperature (°C)", 15.0, 35.0, 24.0, 0.5)
        light_hours = st.slider("Daily Light Hours", 8, 16, 12, 1)
    
    with col2:
        humidity = st.slider("Average Humidity (%)", 40, 90, 65, 5)
        ec_level = st.slider("Nutrient Solution EC (mS/cm)", 1.0, 3.0, 2.0, 0.1)
    
    # Predict button
    if st.button("Generate Prediction"):
        with st.spinner("Generating growth prediction..."):
            # Simulate processing time
            import time
            time.sleep(1)
            
            # Display prediction results (in a real app, this would come from a trained model)
            st.success("Prediction complete!")
            
            st.write("#### Growth Prediction Results")
            
            # Generate prediction data
            days_to_predict = 30
            current_day = days_since_planting
            
            # Simple growth model (would be more sophisticated in a real app)
            days = list(range(current_day - 10 if current_day > 10 else 0, current_day + days_to_predict + 1))
            
            # Height prediction (sigmoid curve)
            max_height = 200  # Maximum height in cm
            growth_rate = 0.1  # Growth rate parameter
            midpoint = 45  # Day at which growth is at midpoint
            
            # Adjust parameters based on environmental factors