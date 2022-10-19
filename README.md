# flask_online_shop
Небольшой магазин на Flask.
Вы можете просматривать товары, добавлять в корзину, оплачивать, оставлять комментарии к товару.

Можете создать свой товар через специальную форму. Есть обычные и вип товары. Вип товары более яркие и всегда находятся наверху страницы.

В проекте вместе с Flask применяются: Flask-SQLAlchemy, Flask-WTF, Flask-Login и другие библиотеки.

Сайт поддерживает регистрацию и авторизацию пользователей.

## Запуск проекта
* Версия python 3.10.7
* Клонируем репозиторий себе в виртуальное окружение `git clone https://github.com/NiatpacBlack/flask_online_shop.git`
* Переходим в папку проекта `cd flask_online_shop`
* Устанавливаем зависимости из requirements.txt: `pip install -r requirements.txt` 
* вводим команду: `flask run` для запуска приложения
* альтернативный вариант для Unix-систем - установите gunicorn `pip3 install gunicorn` и введите команду `gunicorn --bind 127.0.0.1:5000 app:app`, в данном случае приложение будет доступно в локальной сети.
* aльтернативный вариант для Windows - установите waitress `pip install waitress` и введите команду `waitress-serve --listen=127.0.0.1:5000 app:app`

## Превью сайта
![Peek market](https://user-images.githubusercontent.com/84034483/196797408-c453b963-51cb-4999-b7f7-9c2f5d6a4646.gif)
