from flask import Blueprint, request, current_app, g, render_template, flash, redirect, url_for, jsonify
from sqlalchemy.exc import OperationalError
from ..models import Pizza, Pizza_customize
from ..app import db 


bp = Blueprint('bp_menu', __name__)

@bp.route('/menu', methods = ['GET'])
def index_get():
    pizzas = Pizza.query.order_by(
        Pizza.id.asc()
    )
    return render_template('menu.html', pizzas=pizzas)

@bp.route('/menu/customize/<int:page>', methods = ['GET', 'POST'])
def customize(page=0):
    entry = Pizza.query.get_or_404(page)
    if request.method == 'POST':
        is_ham = entry.is_ham
        is_champignons = entry.is_champignons
        is_pepper = entry.is_pepper
        is_olives = entry.is_olives
        is_bacon = entry.is_bacon
        is_corn = entry.is_corn
        is_tuna = entry.is_tuna
        is_pineapple = entry.is_pineapple

        price = 0

        if not entry.is_ham:
            is_ham = bool(request.form.get("ham"))
            if is_ham:
                price += 5
        if not entry.is_champignons:
            is_champignons = bool(request.form.get("champignons"))
            if is_champignons:
                price += 4
        if not entry.is_pepper:
            is_pepper = bool(request.form.get("pepper"))
            if is_pepper:
                price += 3.5
        if not entry.is_olives:
            is_olives = bool(request.form.get("olives"))
            if is_olives:
                price += 4
        if not entry.is_bacon:
            is_bacon = bool(request.form.get("bacon"))
            if is_bacon:
                price += 5
        if not entry.is_corn:
            is_corn = bool(request.form.get("corn"))
            if is_corn:
                price += 3.5
        if not entry.is_tuna:
            is_tuna = bool(request.form.get("tuna")) 
            if is_tuna:
                price += 7
        if not entry.is_pineapple:
            is_pineapple = bool(request.form.get("pineapple"))
            if is_pineapple:
                price += 4

        size = request.form.get("size")
        if size is None:
            size = "50"

        if size == "30":
            price = price + entry.price_30
        elif size == "40":
            price = price + entry.price_40
        elif size == "50":
            price = price + entry.price_50

        custom = Pizza_customize(pizza_name=entry.pizza_name,
                                 is_sauce=entry.is_sauce,
                                 is_cheese=entry.is_cheese,
                                 is_ham=is_ham,
                                 is_champignons=is_champignons,
                                 is_pepper=is_pepper,
                                 is_olives=is_olives,
                                 is_bacon=is_bacon,
                                 is_corn=is_corn,
                                 is_tuna=is_tuna,
                                 is_pineapple=is_pineapple,
                                 size=size,
                                 price=price)

        db.session.add(custom)
        db.session.commit()

        pizzas_in_cart = Pizza_customize.query.order_by(
        Pizza_customize.id.asc()
        )

        return redirect(url_for('bp_cart.index_get'))

    return render_template('customize.html', entry=entry)
