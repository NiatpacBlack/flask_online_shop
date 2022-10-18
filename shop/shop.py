from flask import Blueprint, render_template, request, url_for, redirect, flash

shop = Blueprint("shop", __name__)


@shop.route("/")
def shop_view():
    """Отображает шаблон магазина с товарами."""

    return render_template(
        "shop/shop_page.html",
        title="Онлайн магазин",
    )
