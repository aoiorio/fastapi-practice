from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

from ..config_for_database_url import TEST_SQLALCHEMY_DATABASE_URL
from ..database import Base
from ..main import app
from ..models import Todos, Users
from ..routers.auth import bcrypt_context

from fastapi.testclient import TestClient

import pytest

# this python file is for reuse import codes and so on.

TEST_SQLALCHEMY_DATABASE_URL = TEST_SQLALCHEMY_DATABASE_URL

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    # close db after return db
    try:
        # YIELD means that return something, except the function will return a generator.
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {'username': 'Atomtest', 'id': 1, 'user_role': 'admin'}

client = TestClient(app)


@pytest.fixture
def test_user():
    user = Users(
        id=1,
        username="Atomtest",
        email="atom@gmail.com",
        first_name="Atom",
        last_name="AtoAto",
        hashed_password=bcrypt_context.hash("test1234!"),
        role="admin",
        phone_number="(080)-80-9273-3849"
    )

    db = TestingSessionLocal()
    db.add(user)
    db.commit()

    yield user

    with engine.connect() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()

@pytest.fixture
def test_todo():
    todo = Todos(
        id=1,
        title="Learn the code!",
        description="Need to learn everyday!",
        priority=5,
        complete=False,
        owner_id=1,
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    # Return "todo" and yield won't stop this logic
    yield todo
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM todos;"))
        connection.commit()


