from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, FileField, IntegerField
from wtforms.validators import DataRequired, Length

photos = UploadSet("photos", IMAGES)


class CreateProductForm(FlaskForm):
    """Форма создания нового товара в магазине."""

    title = StringField(
        "Название товара",
        validators=[DataRequired(), Length(max=100)],
        render_kw={
            "class": "form-control form-control-lg",
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
            "class": "form-control-file",
        },
    )
    description = TextAreaField(
        "Краткая информация о товаре",
        validators=[DataRequired(), Length(max=255)],
        render_kw={
            "class": "form-control",
            "placeholder": "",
        },
    )
    text = TextAreaField(
        "Описание товара",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "",
        },
    )
    price = IntegerField(
        'Цена товара',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "",
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
