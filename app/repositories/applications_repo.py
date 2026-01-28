from typing import List, Optional

from app.schemas.applications import Application


class ApplicationsRepository:
    def __init__(self):
        self._applications: List[Application] = []
        self._next_id = 1

    def create(self, app: Application) -> Application:
        app.id = self._next_id
        self._next_id += 1
        self._applications.append(app)
        return app

    def list(self) -> List[Application]:
        return self._applications

    def get_by_id(self, application_id: int) -> Optional[Application]:
        for app in self._applications:
            if app.id == application_id:
                return app
        return None
