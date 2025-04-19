import streamlit as st
from app.views import dashboard, cultivation, plant_analysis, ai_chat, settings
import os

# Set page configuration
st.set_page_config(
    page_title="PyMelonBuddy",
    page_icon="🍈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
def load_css():
    css = """
    <style>
    .main .block-container {
        padding-top: 2rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 4px;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Load custom CSS
load_css()

# Sidebar navigation
st.sidebar.title("PyMelonBuddy 🍈")
st.sidebar.image("app/static/logo.png", use_column_width=True)

# Navigation options
nav_options = [
    "Dashboard",
    "Cultivation Management",
    "Plant Analysis",
    "AI Consultation",
    "Settings"
]

# Navigation selection
nav_selection = st.sidebar.radio("Navigation", nav_options)

# Display selected view
if nav_selection == "Dashboard":
    dashboard.show()
elif nav_selection == "Cultivation Management":
    cultivation.show()
elif nav_selection == "Plant Analysis":
    plant_analysis.show()
elif nav_selection == "AI Consultation":
    ai_chat.show()
elif nav_selection == "Settings":
    settings.show()

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2023 PyMelonBuddy")
st.sidebar.caption("Version 1.0.0")