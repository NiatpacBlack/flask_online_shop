from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import (
    StringField,
    SubmitField,
    TextAreaField,
    FileField,
    IntegerField,
    BooleanField,
)
from wtforms.validators import DataRequired, Length, NumberRange

photos = UploadSet("photos", IMAGES)


class CreateProductForm(FlaskForm):
    """Форма создания нового товара в магазине."""

    title = StringField(
        "Название товара",
        validators=[DataRequired(), Length(max=100)],
        render_kw={
            "class": "form-control form-control-lg mb-4",
            "placeholder": "",
        },
    )
    image = FileField(
        "Изображение товара",
        validators=[
            DataRequired(),
            FileAllowed(photos, "Загрузить можно только изображение"),
        ],
        render_kw={
            "class": "form-control-file mb-4",
        },
    )
    description = TextAreaField(
        "Информация о товаре",
        validators=[DataRequired(), Length(max=255)],
        render_kw={
            "class": "form-control mb-4",
            "placeholder": "",
        },
    )
    price = IntegerField(
        "Цена товара",
        validators=[DataRequired(), NumberRange(min=1, max=100000)],
        render_kw={
            "class": "form-control mb-4",
            "placeholder": "",
        },
    )
    vip_priority = BooleanField(
        "Задать товару VIP статус?",
        render_kw={
            "class": "form-check-input mb-4",
        },
    )
    submit = SubmitField(
        "Добавить",
        render_kw={"class": "btn my-3 btn-primary btn-block"},
    )


class CreateCommentForm(FlaskForm):
    """Форма создания нового комментария."""

    text = TextAreaField(
        "Текст комментария",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "",
        },
    )
    submit = SubmitField(
        "Оставить комментарий",
        render_kw={"class": "btn my-3 btn-primary btn-block"},
    )
