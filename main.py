import streamlit as st
from app.views import dashboard, cultivation, ai_chat, plant_analysis, settings
import config

def main():
    st.set_page_config(
        page_title="PyMelonBuddy",
        page_icon="🍈",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Apply custom CSS for mobile-friendly, modern UI
    with open("app/static/css/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("PyMelonBuddy 🍈")
    
    menu_options = {
        "Dashboard": dashboard.show,
        "Cultivation Management": cultivation.show,
        "AI Consultation": ai_chat.show,
        "Plant Analysis": plant_analysis.show,
        "Settings": settings.show
    }
    
    selection = st.sidebar.radio("Navigate", list(menu_options.keys()))
    
    # Display the selected page
    menu_options[selection]()
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.info("© 2023 PyMelonBuddy")

if __name__ == "__main__":
    main()