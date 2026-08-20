from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class EventStaff(Base):

    __tablename__ = "event_staff"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id"),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    assigned_at: Mapped[datetime] = mapped_column(
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