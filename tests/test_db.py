from sqlalchemy import select

from backend.models import User


def test_create_user(session):
    new_user = User(username='paulo', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'paulo'))

    assert user.username == 'paulo'
