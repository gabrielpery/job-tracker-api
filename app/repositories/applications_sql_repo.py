from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.infrastructure.db.models.application import ApplicationModel
from app.schemas.applications import Application, ApplicationStatus


class ApplicationsSqlRepository:
    def __init__(self, db: Session):
        self._db = db

    def create(self, user_id: int, app: Application) -> Application:
        row = ApplicationModel(
            user_id=user_id,
            company=app.company,
            role=app.role,
            status=app.status.value,
        )
        self._db.add(row)
        self._db.commit()
        self._db.refresh(row)

        return Application(
            id=row.id,
            company=row.company,
            role=row.role,
            status=ApplicationStatus(row.status),
        )

    def list(
        self,
        user_id: int,
        status: Optional[ApplicationStatus],
        limit: int,
        offset: int,
    ) -> List[Application]:
        stmt = select(ApplicationModel).where(
            ApplicationModel.user_id == user_id
        )

        if status is not None:
            stmt = stmt.where(ApplicationModel.status == status.value)

        stmt = (
            stmt
            .order_by(ApplicationModel.id.asc())
            .limit(limit)
            .offset(offset)
        )

        rows = self._db.scalars(stmt).all()

        return [
            Application(
                id=r.id,
                company=r.company,
                role=r.role,
                status=ApplicationStatus(r.status),
            )
            for r in rows
        ]

    def get_by_id(self, user_id: int, application_id: int) -> Optional[Application]:
        row = self._db.scalar(
            select(ApplicationModel).where(
                ApplicationModel.user_id == user_id,
                ApplicationModel.id == application_id,
            )
        )
        if row is None:
            return None

        return Application(
            id=row.id,
            company=row.company,
            role=row.role,
            status=ApplicationStatus(row.status),
        )
