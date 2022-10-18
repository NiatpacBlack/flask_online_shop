from datetime import datetime

from flask_login import UserMixin

from app import db, login_manager


class UserModel(db.Model, UserMixin):
    """Модель пользователя."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), default="user")
    registration_data = db.Column(db.DateTime, default=datetime.utcnow)
    # comments = db.relationship("CommentModel", backref="user_comment", lazy=True)

    def __int__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        """При помощи этого метода мы будем получать соответствующую запись из базы данных."""

        return f"<UserModel {self.id}>"


@login_manager.user_loader
def load_user(user_model_id: str):
    """
    Этот обратный вызов используется для перезагрузки объекта пользователя из eго идентификатора, хранящегося в сеансе.
    Он должен принимать str идентификатор пользователя и возвращать соответствующий объект.
    """

    return UserModel.query.get(user_model_id)
