from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.database import Base


class Event(Base):

    __tablename__ = "events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(255),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    start_time = Column(
        DateTime,
        nullable=False
    )

    end_time = Column(
        DateTime,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    staff_members = relationship(
        "EventStaff",
        back_populates="event",
        cascade="all, delete-orphan"
    )