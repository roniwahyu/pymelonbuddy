# PyMelonBuddy Configuration

# Database settings
DATABASE_URL = "sqlite:///melon_buddy.db"

# API Keys (replace with your actual keys)
GEMINI_API_KEY = "your_gemini_api_key_here"
OPENROUTER_API_KEY = "your_openrouter_api_key_here"

# Default settings
DEFAULT_AI_MODEL = "Gemini"  # Options: "Gemini", "OpenRouter"
DEFAULT_IRRIGATION_TYPES = ["Drip Fertigation", "Ebb and Flow", "Deep Water Culture", "NFT", "Aeroponics"]
DEFAULT_MEDIA_TYPES = ["Cocopeat", "Rockwool", "Perlite", "Vermiculite", "Hydroton"]

# Image analysis settings
IMAGE_ANALYSIS_THRESHOLD = 0.7

# Application paths
UPLOAD_FOLDER = "uploads"
BACKUP_FOLDER = "backups"