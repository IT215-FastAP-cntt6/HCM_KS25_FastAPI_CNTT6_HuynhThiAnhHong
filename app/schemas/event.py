from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EventBase(BaseModel):

    name: str
    description: str | None = None
    start_time: datetime
    end_time: datetime


class EventCreate(EventBase):
    pass


class EventUpdate(BaseModel):

    name: str | None = None
    description: str | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None


class EventResponse(EventBase):

    id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )