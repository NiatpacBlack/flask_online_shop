from wtforms import ValidationError

from .models import UserModel, db


def add_new_user_in_user_table(username: str, email: str, hash_password: str) -> None:
    """
    Добавляет нового пользователя в таблицу UserModel.
    Возвращает строку с информацией об ошибке, если не прошел валидацию.
    """

    db_object = UserModel(
        username=username,
        email=email,
        password=hash_password,
    )
    db.session.add(db_object)
    db.session.commit()


def check_user_in_user_table(username: str):
    """Возвращает запись о пользователе, если его username есть в таблице UserModel."""

    return UserModel.query.filter_by(username=username).first()


def validate_user_in_user_table(message="Пользователь с таким именем уже существует"):
    """Проверяет, есть ли переданные имя пользователя в таблице UserTable."""

    def _validate_user_in_user_table(form, username):
        username_in_table = (
            db.session.query(UserModel)
            .filter(UserModel.username == f"{username.data}")
            .all()
        )
        if username_in_table:
            raise ValidationError(message)

    return _validate_user_in_user_table


def validate_email_in_user_table(message="Пользователь с таким email уже существует"):
    """Проверяет есть ли переданные имя пользователя в таблице UserTable."""

    def _validate_email_in_user_table(form, email):
        email_in_table = (
            db.session.query(UserModel).filter(UserModel.email == f"{email.data}").all()
        )
        if email_in_table:
            raise ValidationError(message)

    return _validate_email_in_user_table
