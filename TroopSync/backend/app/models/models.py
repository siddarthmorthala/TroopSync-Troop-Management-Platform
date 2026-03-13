from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)  # scout, parent, scoutmaster, treasurer, etc.
    email = Column(String, nullable=True)
    patrol = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

class AdvancementRecord(Base):
    __tablename__ = "advancement_records"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)
    advancement_type = Column(String, nullable=False)  # rank or merit_badge
    target_name = Column(String, nullable=False)
    completed_requirements = Column(Integer, default=0)
    total_requirements = Column(Integer, nullable=False)
    status = Column(String, default="in_progress")

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    event_date = Column(Date, nullable=False)
    seats_available = Column(Integer, default=0)
    notes = Column(Text, nullable=True)

class LedgerEntry(Base):
    __tablename__ = "ledger_entries"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=True)
    entry_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class ServiceLog(Base):
    __tablename__ = "service_logs"
    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"), nullable=False)
    project_name = Column(String, nullable=False)
    hours = Column(Float, nullable=False)
    service_date = Column(Date, nullable=False)

class MeritBadgeGuide(Base):
    __tablename__ = "merit_badge_guides"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    requirement_summary = Column(Text, nullable=False)
    resource_link = Column(String, nullable=True)
