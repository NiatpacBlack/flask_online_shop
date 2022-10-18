from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import configure_uploads

from shop.forms import photos
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Настройка приложения Flask."""

    app = Flask(__name__)
    app.config.from_object(Config)

    from authentication.authentication import authentication
    from shop.shop import shop

    app.register_blueprint(authentication, url_prefix="/authentication")
    app.register_blueprint(shop, url_prefix="/")

    configure_uploads(app, photos)

    db.init_app(app)
    login_manager.init_app(app)

    return app


app = create_app()


@app.route('/about')
def about_view():
    """Отображение страницы 'О нас'."""

    return render_template('about_page.html')


@app.route('/contacts')
def contacts_view():
    """Отображение страницы контактов."""

    return render_template('contacts_page.html')


@app.errorhandler(404)
def page_not_found_view(error_text):
    """При получении ошибки 404 отобразит кастомный шаблон с информацией о ней. В консоль вернет 404 ошибку."""

    return render_template("404_page.html", error_text=error_text), 404


if __name__ == '__main__':
    app.run(debug=True)
