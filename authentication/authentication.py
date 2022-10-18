from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from authentication.forms import SignUpForm, SignInForm
from authentication.services import add_new_user_in_user_table, check_user_in_user_table

authentication = Blueprint("authentication", __name__)


@authentication.route("/sign_in", methods=["POST", "GET"])
def sign_in_view():
    """Представление страницы авторизации пользователя."""

    form = SignInForm()

    if form.validate_on_submit():
        username = form.data.get("username")
        password = form.data.get("password")
        user = check_user_in_user_table(username=username)

        if user and check_password_hash(user.password, password):
            login_user(user)
            return _redirect_to_home_or_next_page()
        else:
            flash("Пользователь или пароль не существуют, повторите попытку.", "danger")

    return render_template(
        "authentication/login_page.html",
        form=form,
        title="Вход",
    )


@authentication.route("/sign_out")
@login_required
def sign_out_view():
    """Осуществляет выход пользователя из своего профиля."""

    logout_user()
    return redirect(url_for("shop.shop_view"))


@authentication.route("/sign_up", methods=["POST", "GET"])
def sign_up_view():
    """Представление страницы регистрации пользователя."""

    form = SignUpForm()
    if request.method == "POST" and form.validate_on_submit():
        add_new_user_in_user_table(
            username=request.form.get("username"),
            email=request.form.get("email"),
            hash_password=generate_password_hash(request.form.get("password")),
        )
        user = check_user_in_user_table(username=request.form.get("username"))
        if user:
            login_user(user)
            return _redirect_to_home_or_next_page()

    return render_template(
        "authentication/registration_page.html",
        form=form,
        title="Регистрация",
    )


def _redirect_to_home_or_next_page():
    """Перенаправит на страницу, переданную в аргументе next_page, либо на главную."""

    next_page = request.args.get("next_page")
    return redirect(next_page or url_for("shop.shop_view"))
