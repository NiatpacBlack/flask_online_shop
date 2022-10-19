import os

# Переменная в которую помещается исполняемая директория скрипта
_basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Описание всех конфигурационных настроек приложения."""

    # Режим отладки
    DEBUG = True

    # Секретный ключ задается либо в переменной окружения либо непосредственно.
    SECRET_KEY = os.environ.get("SECRET_KEY") or "any_key"

    # Папка для загруженных файлов
    UPLOADED_PHOTOS_DEST = os.path.join(_basedir, "static/media/img")

    # Опции подключения к SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(_basedir, "shop.db")
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Потоки на 4 ядра
    THREADS_PER_PAGE = 8

    # CSRF настройки, защищают от подмены POST-сообщений
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"

    # Используется для входящего в WTForms поля RecaptchaField. Подробности в документации:
    # https://flask-wtf.readthedocs.io/en/1.0.x/form/#recaptcha
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = "6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J"
    RECAPTCHA_PRIVATE_KEY = "6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu"
    RECAPTCHA_OPTIONS = {"theme": "white"}
