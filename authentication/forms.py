from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from authentication.services import (
    validate_user_in_user_table,
    validate_email_in_user_table,
)


class SignUpForm(FlaskForm):
    """Форма регистрации нового пользователя."""

    username = StringField(
        "Имя пользователя",
        validators=[
            DataRequired(),
            Length(max=255),
            validate_user_in_user_table(),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Имя пользователя",
        },
    )
    email = StringField(
        "Email",
        validators=[
            Email(message="Введенный email некорректен"),
            DataRequired(),
            Length(max=255),
            validate_email_in_user_table(),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Email",
        },
    )

    password = PasswordField(
        "Пароль",
        validators=[DataRequired(), Length(max=255)],
        render_kw={
            "class": "form-control help",
            "placeholder": "Пароль",
        },
    )
    repeat_password = PasswordField(
        "Повтор пароля",
        validators=[DataRequired(), EqualTo("password", message="Пароли не совпадают")],
        render_kw={
            "class": "form-control help",
            "placeholder": "Повтор пароля",
        },
    )
    submit = SubmitField(
        "Зарегистрироваться",
        render_kw={"class": "btn btn-success"},
    )


class SignInForm(FlaskForm):
    """Форма авторизации пользователя."""

    username = StringField(
        "Имя пользователя",
        validators=[
            DataRequired(),
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Имя пользователя",
        },
    )
    password = PasswordField(
        "Пароль",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control help",
            "placeholder": "Пароль",
        },
    )
    submit = SubmitField(
        "Вход",
        render_kw={"class": "btn btn-info btn-lg"},
    )
