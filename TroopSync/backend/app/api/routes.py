from datetime import date
from fastapi import APIRouter
from app.schemas.schemas import AdvancementCheckRequest, EventCreate, LedgerCreate, MemberCreate, ServiceCreate
from app.services.rules import passes_advancement_rules

router = APIRouter()

MEMBERS = [
    {"id": 1, "name": "Aidan Brooks", "role": "scout", "email": "aidan@example.com", "patrol": "Raven", "is_active": True},
    {"id": 2, "name": "Chris Patel", "role": "treasurer", "email": "chris@example.com", "patrol": None, "is_active": True},
]
EVENTS = [
    {"id": 1, "title": "Lake Ray Roberts Campout", "category": "campout", "event_date": date(2026, 4, 18), "seats_available": 12, "notes": "Spring troop outing"}
]
LEDGER = []
SERVICE_LOGS = []

@router.get('/health')
def health():
    return {"status": "ok", "app": "TroopSync"}

@router.get('/dashboard')
def dashboard():
    return {
        "troop": "Troop 261",
        "city": "Plano, TX",
        "members": len(MEMBERS),
        "events": len(EVENTS),
        "open_tasks": 7,
        "low_balances": 3,
        "service_hours_this_month": 42.5,
    }

@router.get('/members')
def list_members():
    return MEMBERS

@router.post('/members')
def create_member(member: MemberCreate):
    new = {"id": len(MEMBERS)+1, **member.model_dump(), "is_active": True}
    MEMBERS.append(new)
    return new

@router.post('/advancement/check')
def advancement_check(payload: AdvancementCheckRequest):
    return passes_advancement_rules(payload.completed_requirements, payload.total_requirements)

@router.get('/events')
def list_events():
    return EVENTS

@router.post('/events')
def create_event(event: EventCreate):
    new = {"id": len(EVENTS)+1, **event.model_dump()}
    EVENTS.append(new)
    return new

@router.post('/ledger')
def add_ledger_entry(entry: LedgerCreate):
    item = {"id": len(LEDGER)+1, **entry.model_dump()}
    LEDGER.append(item)
    return item

@router.get('/ledger/summary')
def ledger_summary():
    balance = sum(x['amount'] if x['entry_type']=='credit' else -x['amount'] for x in LEDGER)
    return {"entries": len(LEDGER), "net_balance": balance}

@router.post('/service')
def add_service_log(log: ServiceCreate):
    item = {"id": len(SERVICE_LOGS)+1, **log.model_dump()}
    SERVICE_LOGS.append(item)
    return item

@router.get('/communications/templates')
def templates():
    return [
        {"name": "Campout Reminder", "channel": "email"},
        {"name": "Carpool Reminder", "channel": "sms"},
        {"name": "Fundraiser Shift Reminder", "channel": "email"},
    ]

@router.get('/merit-badges')
def merit_badges():
    return [
        {"name": "Camping", "summary": "Track nights, gear prep, and outdoor skills.", "resource_link": "https://www.scouting.org/"},
        {"name": "Citizenship in the Community", "summary": "Community engagement and civic awareness.", "resource_link": "https://www.scouting.org/"},
    ]
