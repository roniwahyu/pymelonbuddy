from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class GrowingMedia(Base):
    __tablename__ = 'growing_media'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    water_retention = Column(Float)  # Scale 1-10
    aeration = Column(Float)  # Scale 1-10
    ph_level = Column(Float)
    ec_level = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    # Relationships
    plants = relationship("Plant", back_populates="media")
    
    def __repr__(self):
        return f"<GrowingMedia(name='{self.name}', water_retention={self.water_retention})>"
    
    @classmethod
    def get_default_media(cls, session):
        """Return default media types or create them if they don't exist"""
        from config import DEFAULT_MEDIA_TYPES
        
        existing_media = session.query(cls).all()
        if not existing_media:
            for media_name in DEFAULT_MEDIA_TYPES:
                # Default values - would be customized in a real application
                new_media = cls(
                    name=media_name,
                    description=f"Default description for {media_name}",
                    water_retention=5.0,
                    aeration=5.0,
                    ph_level=6.0,
                    ec_level=1.5
                )
                session.add(new_media)
            session.commit()
            return session.query(cls).all()
        return existing_media