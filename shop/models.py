from datetime import datetime

from pytz import timezone

from app import db


class ProductModel(db.Model):
    """Таблица, описывающая поля товара. Данными товарами будет наполнен сайт."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_data = db.Column(
        db.DateTime, default=datetime.now(timezone("Europe/Minsk"))
    )
    is_active = db.Column(db.Boolean, default=True)
    vip_priority = db.Column(db.Boolean, default=False)

    def __int__(self, title, description, text, price):
        self.title = title
        self.description = description
        self.text = text
        self.price = price

    def __repr__(self):
        return f"<ProductModel {self.id} vip {self.vip_priority}>"


class CommentModel(db.Model):
    """Таблица, хранящая данные о комментариях под конкретным товаром."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product_model.id", ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey("user_model.id", ondelete="CASCADE"))
    text = db.Column(db.Text, nullable=False)
    created_data = db.Column(
        db.DateTime, default=datetime.now(timezone("Europe/Minsk"))
    )

    def __repr__(self):
        return f"<CommentModel {self.id}>"
