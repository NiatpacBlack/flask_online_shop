from app import db
from authentication.models import UserModel
from shop.models import ProductModel, CommentModel


def add_product_in_product_model(product: dict[str]) -> None:
    """Добавляет данные из словаря product в таблицу ProductModel."""

    db_object = ProductModel(
        title=product["title"],
        image=product["image"],
        description=product["description"],
        text=product["text"],
        price=product["price"],
    )
    db.session.add(db_object)
    db.session.commit()


def get_all_products_from_product_model_on_page(page: int):
    """
    Возвращает QuerySet состоящий из всех продуктов из таблицы ProductModel.

    Продукты соответствуют текущей странице page.
    """

    return ProductModel.query.order_by(ProductModel.id.desc()).paginate(page=page, per_page=9)


def get_product_from_product_model_where_id(product_id: int):
    """Возвращает QuerySet и информацией о товаре из магазина с id равным аргументу product_id."""

    return ProductModel.query.get(product_id)


def get_five_last_products_from_product_table(product_id: int):
    """Возвращает QuerySet пяти последних товаров из таблицы ProductModel без текущего с product_id."""

    return ProductModel.query.filter(ProductModel.id != product_id).limit(5)[::-1]


def add_comment_in_comments_table(comment: dict[str]) -> None:
    """Добавляет данные из словаря comment в таблицу CommentModel."""

    db_object = CommentModel(
        post_id=comment["post_id"],
        user_id=comment["user_id"],
        text=comment["text"],
    )
    db.session.add(db_object)
    db.session.commit()


def get_comments_from_comments_table_where_post_id(product_id: int):
    """
    Возвращает QuerySet из всех комментариев к товару с id product_id в обратном порядке.

    В данной функции реализуется объединение всех комментариев к товару с таблицей пользователей, чтобы
    выводить их username над комментарием в шаблоне.
    """

    return (
        db.session.query(UserModel, CommentModel)
        .join(CommentModel, UserModel.id == CommentModel.user_id)
        .filter_by(product_id=product_id)[::-1]
    )

