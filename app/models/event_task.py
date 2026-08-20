from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text
)
from sqlalchemy.orm import relationship

from app.db.database import Base


class EventTask(Base):

    __tablename__ = "event_tasks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    event_staff_id = Column(
        Integer,
        ForeignKey("event_staff.id"),
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    status = Column(
        String(50),
        default="pending",
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    staff = relationship(
        "EventStaff",
        back_populates="tasks"
    )