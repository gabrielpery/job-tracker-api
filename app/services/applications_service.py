from typing import List, Optional
from app.schemas.applications import Application, ApplicationCreate, ApplicationStatus


class ApplicationsService:
    def __init__(self, repo):
        self._repo = repo

    def create_application(self, user_id: int, payload: ApplicationCreate) -> Application:
        company = payload.company.strip()
        role = payload.role.strip()

        app_obj = Application(
            id=0,
            company=company,
            role=role,
            status=payload.status,
        )
        return self._repo.create(user_id=user_id, app=app_obj)

    def list_applications(
        self,
        user_id: int,
        status: Optional[ApplicationStatus],
        limit: int,
        offset: int,
    ) -> List[Application]:
        return self._repo.list(
            user_id=user_id,
            status=status,
            limit=limit,
            offset=offset,
        )

    def get_application(self, user_id: int, application_id: int) -> Application | None:
        return self._repo.get_by_id(user_id=user_id, application_id=application_id)
