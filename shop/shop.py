from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    abort,
    session,
    flash,
)
from flask_login import login_required, current_user

from shop.forms import CreateProductForm, photos, CreateCommentForm
from shop.services import (
    add_product_in_product_model,
    get_all_products_from_product_model_on_page,
    get_product_from_product_model_where_id,
    add_comment_in_comments_table,
    get_five_last_products_from_product_table,
    get_comments_from_comments_table_where_post_id,
    get_total_price_of_products_in_cart,
)

shop = Blueprint("shop", __name__)


@shop.route("/", methods=["GET", "POST"])
def shop_view():
    """Отображает шаблон магазина с товарами разделенными пагинацией."""

    page = request.args.get("page")
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    return render_template(
        "shop/shop_page.html",
        title="Онлайн магазин",
        products_for_page=get_all_products_from_product_model_on_page(page=page),
    )


@shop.route("/create_product", methods=["GET", "POST"])
@login_required
def create_product_view():
    """Отображение страницы с формой создания нового товара."""

    form = CreateProductForm()

    if request.method == "POST":

        product = {
            "title": request.form.get("title"),
            "image": photos.save(form.image.data),
            "description": request.form.get("description"),
            "price": request.form.get("price"),
            "vip_priority": request.form.get("vip_priority"),
        }

        add_product_in_product_model(product)

        return redirect(url_for("shop.shop_view"))

    return render_template(
        "shop/create_product_page.html", title="Онлайн магазин", form=form
    )


@shop.route("/product-<int:product_id>", methods=["GET", "POST"])
def product_page_view(product_id):
    """
    Страница отображающая полную информацию о конкретном товаре.

    На странице реализован функционал добавления товара в сессию пользователя при нажатии кнопки 'Добавить в корзину'.
    Дополнительно на странице отображаются пять последних товаров из таблицы ProductModel без текущего поста.
    """

    comment_form = CreateCommentForm()

    if not get_product_from_product_model_where_id(product_id):
        abort(404)

    if request.method == "POST":
        if request.form.get("product_count"):
            product_object = get_product_from_product_model_where_id(product_id)
            product_object = {
                "title": product_object.title,
                "price": product_object.price,
                "count": request.form.get("product_count"),
                "sum": int(product_object.price) * int(request.form.get("product_count")),
            }
            if "product_data" not in session:
                session["product_data"] = [product_object]
            else:
                session["product_data"].append(product_object)
                session.modified = True

        if request.form.get("text"):
            comment = {
                "product_id": product_id,
                "user_id": current_user.id,
                "text": request.form.get("text"),
            }
            add_comment_in_comments_table(comment)

    return render_template(
        "shop/product_page.html",
        product=get_product_from_product_model_where_id(product_id),
        five_last_products=get_five_last_products_from_product_table(product_id),
        comment_form=comment_form,
        all_comments=get_comments_from_comments_table_where_post_id(product_id),
    )


@shop.route("/shopping_cart", methods=["GET", "POST"])
@login_required
def shopping_cart_view():
    """
    Отображение страницы корзины товаров.

    Данные о товарах в корзине получаем из текущей сессии пользователя. Из поля 'product_data'.
    В шаблоне реализуем формы, с помощью который можно очистить корзину и оформить оплату.
    """

    total_price = 0
    if "product_data" in session:

        total_price = get_total_price_of_products_in_cart()

        if request.method == "POST":
            if request.form.get("cart_clear"):
                del session["product_data"]
            if request.form.get("cart_confirm"):
                del session["product_data"]
                flash("Оплата прошла успешно.", "success")

    return render_template(
        "shop/shopping_cart_page.html",
        title="Корзина товаров",
        total_price=total_price,
    )


@shop.route("/about")
def about_view():
    """Отображение страницы 'О нас'."""

    return render_template("shop/about_page.html")
