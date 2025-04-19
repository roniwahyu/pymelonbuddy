from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
import hashlib
import os

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    salt = Column(String(32), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    
    # Relationships
    plants = relationship("Plant", back_populates="user")
    chat_history = relationship("ChatHistory", back_populates="user")
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
    
    def set_password(self, password):
        """Set password with salt and hashing"""
        self.salt = os.urandom(16).hex()
        self.password_hash = self._hash_password(password, self.salt)
    
    def verify_password(self, password):
        """Verify password against stored hash"""
        return self.password_hash == self._hash_password(password, self.salt)
    
    def _hash_password(self, password, salt):
        """Hash password with salt using SHA-256"""
        return hashlib.pbkdf2_hmac(
            'sha256', 
            password.encode('utf-8'), 
            bytes.fromhex(salt), 
            100000
        ).hex()
    
    def update_last_login(self):
        """Update the last login timestamp"""
        self.last_login = datetime.datetime.utcnow()


class ChatHistory(Base):
    __tablename__ = 'chat_history'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    query = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    model_used = Column(String(50))  # Which AI model was used
    
    # Relationship
    user = relationship("User", back_populates="chat_history")
    
    def __repr__(self):
        return f"<ChatHistory(user_id={self.user_id}, timestamp='{self.timestamp}')>"