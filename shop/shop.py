from flask import Blueprint, render_template, request, url_for, redirect, abort
from flask_login import login_required, current_user

from shop.forms import CreateProductForm, photos, CreateCommentForm
from shop.services import add_product_in_product_model, get_all_products_from_product_model_on_page, \
    get_product_from_product_model_where_id, add_comment_in_comments_table, get_five_last_products_from_product_table, \
    get_comments_from_comments_table_where_post_id

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
        products_for_page=get_all_products_from_product_model_on_page(page=page)
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
            "text": request.form.get("text"),
            "price": request.form.get('price'),
        }
        add_product_in_product_model(product)
        return redirect(url_for("shop.shop_view"))

    return render_template(
        "shop/create_product_page.html",
        title="Онлайн магазин",
        form=form
    )


@shop.route("/product-<int:product_id>", methods=["GET", "POST"])
def product_page_view(product_id):
    """
    Страница отображающая полную информацию о конкретном товаре.
    Дополнительно на странице отображаются пять последних товаров из таблицы ProductModel без текущего поста.
    """

    comment_form = CreateCommentForm()

    if not get_product_from_product_model_where_id(product_id):
        abort(404)

    if request.method == "POST" and comment_form.validate_on_submit():
        comment = {
            "product_id": product_id,
            "user_id": current_user.id,
            "text": request.form.get("text"),
        }
        add_comment_in_comments_table(comment)
    return render_template(
        "shop/product_page.html",
        post=get_product_from_product_model_where_id(product_id),
        five_last_posts=get_five_last_products_from_product_table(product_id),
        comment_form=comment_form,
        all_comments=get_comments_from_comments_table_where_post_id(product_id),
    )
