from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Plant(Base):
    __tablename__ = 'plants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    variety = Column(String(100))
    planting_date = Column(DateTime, default=datetime.datetime.utcnow)
    harvest_date = Column(DateTime, nullable=True)
    
    # Foreign keys
    media_id = Column(Integer, ForeignKey('growing_media.id'))
    irrigation_id = Column(Integer, ForeignKey('irrigation_systems.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # Plant metrics
    current_height = Column(Float, default=0.0)  # in cm
    stem_diameter = Column(Float, default=0.0)  # in mm
    leaf_count = Column(Integer, default=0)
    fruit_count = Column(Integer, default=0)
    
    # Status
    is_active = Column(Boolean, default=True)
    health_status = Column(String(50), default="Good")
    notes = Column(Text)
    
    # Relationships
    media = relationship("GrowingMedia", back_populates="plants")
    irrigation = relationship("IrrigationSystem", back_populates="plants")
    user = relationship("User", back_populates="plants")
    measurements = relationship("PlantMeasurement", back_populates="plant")
    analyses = relationship("PlantAnalysis", back_populates="plant")
    
    def __repr__(self):
        return f"<Plant(name='{self.name}', variety='{self.variety}')>"
    
    def calculate_age(self):
        """Calculate the age of the plant in days"""
        today = datetime.datetime.utcnow()
        return (today - self.planting_date).days
    
    def update_measurements(self, height=None, stem_diameter=None, leaf_count=None, fruit_count=None):
        """Update plant measurements and create a measurement record"""
        if height is not None:
            self.current_height = height
        if stem_diameter is not None:
            self.stem_diameter = stem_diameter
        if leaf_count is not None:
            self.leaf_count = leaf_count
        if fruit_count is not None:
            self.fruit_count = fruit_count
            
        # Create a measurement record
        measurement = PlantMeasurement(
            plant_id=self.id,
            height=self.current_height,
            stem_diameter=self.stem_diameter,
            leaf_count=self.leaf_count,
            fruit_count=self.fruit_count
        )
        return measurement


class PlantMeasurement(Base):
    __tablename__ = 'plant_measurements'
    
    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey('plants.id'))
    measurement_date = Column(DateTime, default=datetime.datetime.utcnow)
    height = Column(Float)  # in cm
    stem_diameter = Column(Float)  # in mm
    leaf_count = Column(Integer)
    fruit_count = Column(Integer)
    
    # Environmental conditions at measurement time
    temperature = Column(Float, nullable=True)  # in Celsius
    humidity = Column(Float, nullable=True)  # percentage
    light_level = Column(Float, nullable=True)  # in lux
    
    # Relationship
    plant = relationship("Plant", back_populates="measurements")
    
    def __repr__(self):
        return f"<PlantMeasurement(plant_id={self.plant_id}, date='{self.measurement_date}')>"