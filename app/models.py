from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


DATABASE_URL = "sqlite:///./logs/translation.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class TranslationLog(Base):
    __tablename__ = "translation"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    original_text = Column(String, nullable=True)
    target_language = Column(String, nullable=True)
    request_type = Column(String)
    endpoint = Column(String)
    translated_text = Column(String, nullable=True)

    def save(self):
        db = SessionLocal()
        db.add(self)
        db.commit()
        db.close()


Base.metadata.create_all(bind=engine)
