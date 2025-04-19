from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class IrrigationSystem(Base):
    __tablename__ = 'irrigation_systems'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    flow_rate = Column(Float)  # liters per hour
    pressure = Column(Float)  # in kPa
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    # Relationships
    plants = relationship("Plant", back_populates="irrigation")
    schedules = relationship("IrrigationSchedule", back_populates="system")
    
    def __repr__(self):
        return f"<IrrigationSystem(name='{self.name}', flow_rate={self.flow_rate})>"
    
    @classmethod
    def get_default_systems(cls, session):
        """Return default irrigation systems or create them if they don't exist"""
        from config import DEFAULT_IRRIGATION_TYPES
        
        existing_systems = session.query(cls).all()
        if not existing_systems:
            for system_name in DEFAULT_IRRIGATION_TYPES:
                # Default values - would be customized in a real application
                new_system = cls(
                    name=system_name,
                    description=f"Default description for {system_name}",
                    flow_rate=2.0,
                    pressure=100.0
                )
                session.add(new_system)
            session.commit()
            return session.query(cls).all()
        return existing_systems


class IrrigationSchedule(Base):
    __tablename__ = 'irrigation_schedules'
    
    id = Column(Integer, primary_key=True)
    system_id = Column(Integer, ForeignKey('irrigation_systems.id'))
    start_time = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False)  # in minutes
    frequency = Column(String(50))  # daily, every 2 days, etc.
    nutrient_mix_id = Column(Integer, ForeignKey('nutrient_mixes.id'), nullable=True)
    ec_target = Column(Float)  # target EC level
    ph_target = Column(Float)  # target pH level
    
    # Relationships
    system = relationship("IrrigationSystem", back_populates="schedules")
    nutrient_mix = relationship("NutrientMix")
    
    def __repr__(self):
        return f"<IrrigationSchedule(system_id={self.system_id}, start_time='{self.start_time}')>"


class NutrientMix(Base):
    __tablename__ = 'nutrient_mixes'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    nitrogen = Column(Float)  # in ppm
    phosphorus = Column(Float)  # in ppm
    potassium = Column(Float)  # in ppm
    calcium = Column(Float)  # in ppm
    magnesium = Column(Float)  # in ppm
    sulfur = Column(Float)  # in ppm
    iron = Column(Float)  # in ppm
    manganese = Column(Float)  # in ppm
    zinc = Column(Float)  # in ppm
    copper = Column(Float)  # in ppm
    boron = Column(Float)  # in ppm
    molybdenum = Column(Float)  # in ppm
    
    def __repr__(self):
        return f"<NutrientMix(name='{self.name}')>"