from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Boolean, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class PlantAnalysis(Base):
    __tablename__ = 'plant_analyses'
    
    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey('plants.id'))
    analysis_date = Column(DateTime, default=datetime.datetime.utcnow)
    image_data = Column(LargeBinary, nullable=True)  # Store the image or a reference
    image_path = Column(String(255), nullable=True)  # Alternative: store path to image
    
    # Analysis results
    health_score = Column(Float)  # 0-100 scale
    disease_detected = Column(Boolean, default=False)
    disease_name = Column(String(100), nullable=True)
    disease_confidence = Column(Float, nullable=True)  # 0-1 scale
    
    # Nutrient deficiencies
    nitrogen_status = Column(String(20), nullable=True)  # Deficient, Optimal, Excessive
    phosphorus_status = Column(String(20), nullable=True)
    potassium_status = Column(String(20), nullable=True)
    calcium_status = Column(String(20), nullable=True)
    magnesium_status = Column(String(20), nullable=True)
    
    # AI analysis
    ai_model_used = Column(String(50))
    analysis_summary = Column(Text)
    recommendations = Column(Text)
    
    # Relationships
    plant = relationship("Plant", back_populates="analyses")
    
    def __repr__(self):
        return f"<PlantAnalysis(plant_id={self.plant_id}, health_score={self.health_score})>"
    
    def get_nutrient_status_summary(self):
        """Return a summary of nutrient statuses"""
        statuses = {
            "Nitrogen": self.nitrogen_status,
            "Phosphorus": self.phosphorus_status,
            "Potassium": self.potassium_status,
            "Calcium": self.calcium_status,
            "Magnesium": self.magnesium_status
        }
        
        # Filter out None values
        return {k: v for k, v in statuses.items() if v is not None}