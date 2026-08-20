from sqlalchemy.orm import Session
from app.models.event import Event


def get_event_by_id(
    db: Session,
    event_id: int
) -> Event | None:

    return db.query(Event).filter(
        Event.id == event_id
    ).first()