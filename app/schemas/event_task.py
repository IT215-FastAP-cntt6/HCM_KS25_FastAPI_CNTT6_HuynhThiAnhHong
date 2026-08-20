from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EventTaskBase(BaseModel):

    event_staff_id: int
    title: str
    description: str | None = None


class EventTaskCreate(EventTaskBase):
    pass


class EventTaskUpdate(BaseModel):

    title: str | None = None
    description: str | None = None
    status: str | None = None


class EventTaskResponse(EventTaskBase):

    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )