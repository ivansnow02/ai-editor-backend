from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db import Base


class ImageModel(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    path = Column(String, unique=True, index=True)
    description = Column(String, default="")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="images")
