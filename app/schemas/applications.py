from enum import Enum
from pydantic import BaseModel

from fastapi import Depends
from app.security.current_user import get_current_user_id



class ApplicationStatus(str, Enum):
    applied = "applied"
    interview = "interview"
    offer = "offer"
    rejected = "rejected"

class ApplicationCreate(BaseModel):
    company: str
    role: str
    status: str = "applied"
    status: ApplicationStatus = ApplicationStatus.applied

class Application(ApplicationCreate):
    id: int
