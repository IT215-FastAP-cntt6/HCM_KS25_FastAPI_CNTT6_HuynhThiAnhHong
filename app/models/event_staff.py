from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.orm import relationship

from app.db.database import Base


class EventStaff(Base):

    __tablename__ = "event_staff"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    event_id = Column(
        Integer,
        ForeignKey("events.id"),
        nullable=False
    )

    role = Column(
        String(100),
        nullable=False
    )

    assigned_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user = relationship(
        "User",
        back_populates="event_staff"
    )

    event = relationship(
        "Event",
        back_populates="staff_members"
    )

    tasks = relationship(
        "EventTask",
        back_populates="staff",
        cascade="all, delete-orphan"
    )