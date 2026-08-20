from sqlalchemy.orm import Session
from app.models.event_task import EventTask

def get_task_by_id(
    db: Session,
    task_id: int
) -> EventTask | None:

    return db.query(EventTask).filter(
        EventTask.id == task_id
    ).first()