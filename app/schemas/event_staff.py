from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EventStaffBase(BaseModel):

    user_id: int
    event_id: int
    role: str


class EventStaffCreate(EventStaffBase):
    pass


class EventStaffUpdate(BaseModel):

    role: str | None = None


class EventStaffResponse(EventStaffBase):

    id: int
    assigned_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )