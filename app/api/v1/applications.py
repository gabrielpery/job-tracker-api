from typing import List, Optional


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.infrastructure.db.deps import get_db
from app.repositories.applications_sql_repo import ApplicationsSqlRepository
from app.schemas.applications import Application, ApplicationCreate
from app.schemas.applications import ApplicationStatus
from app.services.applications_service import ApplicationsService

from fastapi import Depends
from app.security.current_user import get_current_user_id


router = APIRouter(prefix="/applications", tags=["applications"])


def get_service(db: Session) -> ApplicationsService:
    repo = ApplicationsSqlRepository(db)
    return ApplicationsService(repo)


@router.post("", response_model=Application)
def create_application(payload: ApplicationCreate,db: Session = Depends(get_db),user_id: int = Depends(get_current_user_id)):
    service = get_service(db)
    return service.create_application(user_id=user_id, payload=payload)



@router.get("", response_model=List[Application])
def list_applications(status: Optional[ApplicationStatus] = None,limit: int = 20,offset: int = 0,db: Session = Depends(get_db),user_id: int = Depends(get_current_user_id)):
    service = get_service(db)
    return service.list_applications(
        user_id=user_id,
        status=status,
        limit=limit,
        offset=offset,
    )


@router.get("/{application_id}", response_model=Application)
def get_application(application_id: int,db: Session = Depends(get_db),user_id: int = Depends(get_current_user_id)):
    service = get_service(db)
    app_obj = service.get_application(user_id=user_id, application_id=application_id)
    if app_obj is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_obj
