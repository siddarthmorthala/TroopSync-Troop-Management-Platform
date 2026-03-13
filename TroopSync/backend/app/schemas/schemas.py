from datetime import date
from pydantic import BaseModel

class MemberCreate(BaseModel):
    name: str
    role: str
    email: str | None = None
    patrol: str | None = None

class MemberOut(MemberCreate):
    id: int
    is_active: bool
    class Config:
        from_attributes = True

class AdvancementCheckRequest(BaseModel):
    completed_requirements: int
    total_requirements: int

class EventCreate(BaseModel):
    title: str
    category: str
    event_date: date
    seats_available: int = 0
    notes: str | None = None

class EventOut(EventCreate):
    id: int
    class Config:
        from_attributes = True

class LedgerCreate(BaseModel):
    member_id: int | None = None
    entry_type: str
    amount: float
    description: str

class ServiceCreate(BaseModel):
    member_id: int
    project_name: str
    hours: float
    service_date: date
