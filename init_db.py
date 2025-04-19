from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config
from app.models.plant import Base as PlantBase
from app.models.user import Base as UserBase
from app.models.irrigation import Base as IrrigationBase
from app.models.analysis import Base as AnalysisBase
import os

def init_database():
    """Initialize the database with tables"""
    engine = create_engine(config.DATABASE_URL)
    
    # Create all tables
    PlantBase.metadata.create_all(engine)
    UserBase.metadata.create_all(engine)
    IrrigationBase.metadata.create_all(engine)
    AnalysisBase.metadata.create_all(engine)
    
    print("Database initialized successfully!")
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Add default data if needed
    # For example, default irrigation systems
    from app.models.irrigation import IrrigationSystem
    IrrigationSystem.get_default_systems(session)
    
    session.close()

if __name__ == "__main__":
    # Create database directory if it doesn't exist
    db_path = os.path.dirname(config.DATABASE_URL.replace("sqlite:///", ""))
    if db_path and not os.path.exists(db_path):
        os.makedirs(db_path)
    
    # Initialize the database
    init_database()