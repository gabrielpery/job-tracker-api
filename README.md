# Job Tracker API

A backend API built to demonstrate practical backend engineering skills using Python.

This project focuses on how real services are typically structured in production environments: authenticated users, clear separation of concerns, database migrations, automated testing, and continuous integration. The emphasis is on correctness, maintainability, and security rather than just making endpoints work.

---

## What this project does

* Users can register and log in securely
* Authenticated users can manage their own job applications
* Each user only ever sees their own data
* Applications can be filtered and paginated
* The database schema is versioned with migrations
* The codebase is tested and verified in CI

---

## Tech used

* Python 3.11
* FastAPI
* SQLAlchemy + Alembic
* SQLite (local development)
* JWT authentication
* Pytest
* GitHub Actions

---

## Structure

The code is split into clear layers:

* **API / routers** – HTTP and request handling
* **Services** – business logic
* **Repositories** – database access
* **Schemas** – request and response models
* **Security** – auth, JWT, password hashing

This keeps concerns separated and makes the project easier to test and extend.

---

## Authentication

* Passwords are hashed with bcrypt
* Login returns a JWT access token
* Tokens are required for protected endpoints
* User identity is derived from the token, not from client input

---

## API overview

Auth:

* POST /api/v1/auth/register
* POST /api/v1/auth/login

Applications (protected):

* POST /api/v1/applications
* GET /api/v1/applications
* GET /api/v1/applications/{id}

The applications list endpoint supports query parameters for filtering and pagination.

---

## Running locally

```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

Interactive docs are available at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Tests and CI

* Tests are written with pytest
* A separate test database is used
* GitHub Actions runs the test suite on every push and PR

---

## Why I built this

I built this project to get comfortable with how backend systems are usually structured in practice: auth, data ownership, migrations, and tests all working together.

---

## References and Acknowledgements

This project was built using official documentation and community resources commonly used in professional backend development, including:

* FastAPI documentation
* SQLAlchemy and Alembic documentation
* Python and Pydantic documentation
* Community discussions and examples from Stack Overflow and GitHub issues

---

## Author

Gabriel Pery