import os
import sys
import subprocess

def main():
    """Run the PyMelonBuddy application"""
    print("Starting PyMelonBuddy...")
    
    # Check if database exists, if not initialize it
    if not os.path.exists("melon_buddy.db"):
        print("Initializing database...")
        subprocess.run([sys.executable, "init_db.py"])
    
    # Create required directories
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("backups", exist_ok=True)
    os.makedirs("app/static", exist_ok=True)
    
    # Run the Streamlit app
    subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    main()