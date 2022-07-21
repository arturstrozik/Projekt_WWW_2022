from flask import Blueprint, request, current_app, g, render_template, flash, redirect, url_for, jsonify, json, Flask
from sqlalchemy.exc import OperationalError
from ..models import Pizza, Pizza_customize, Order
from ..app import db 


bp = Blueprint('bp_cart', __name__)

@bp.route('/cart', methods=['GET', 'POST'])
def index_get():
    pizzas_in_cart = Pizza_customize.query.order_by(
    Pizza_customize.id.asc()
    )
    is_null = db.session.execute("SELECT * FROM pizza_customize")
    counter = 0
    for result in is_null:
        counter += 1
    
    cur = db.session.execute("SELECT * FROM pizza_customize")
    order_value = 0.0
    for result in cur:
         order_value += float(result['price'])

    return render_template('cart.html', pizzas_in_cart=pizzas_in_cart, is_null=counter, value=order_value)

@bp.route('/cart/payment', methods=['GET', 'POST'])
def cart_go_to_payment():
    if request.method == 'POST':
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")
        city = request.form.get("city")

        pizzas = Pizza_customize.query.order_by(
        Pizza.id.asc()
        )

        cur = db.session.execute("SELECT * FROM pizza_customize")
        pizza_customize = ""
        order_value = 0.0
        for result in cur:
            ingredients= "sos, ser"
            if bool(result['is_ham']):
                ingredients += ", szynka"
            if bool(result['is_champignons']):
                ingredients += ", pieczarki"
            if bool(result['is_pepper']):
                            ingredients += ", papryka"
            if bool(result['is_olives']):
                            ingredients += ", oliwki"
            if bool(result['is_bacon']):
                            ingredients += ", bekon"
            if bool(result['is_corn']):
                            ingredients += ", kukurydza"
            if bool(result['is_tuna']):
                            ingredients += ", tuńczyk"
            if bool(result['is_pineapple']):
                            ingredients += ", ananas"

            content = '{"name": "' + result['pizza_name'] + '", ' + '"rozmiar": "' + str(result['size']) + '" "ingredients": "' + ingredients + '" }\n'
            pizza_customize += content
            order_value += float(result['price'])
            
        ordered_pizzas = pizza_customize
        
        order = Order(first_name=first_name,
                      last_name=last_name,
                      phone_number=phone,
                      email=email,
                      city=city,
                      street_and_house_number=address,
                      ordered_pizzas=ordered_pizzas,
                      order_value=order_value,
                      is_paid=False)
        
        db.session.add(order)
        db.session.commit()

        order = db.session.query(Order).order_by(Order.id.desc()).first()
        pizzas_in_cart = Pizza_customize.query.order_by(Pizza_customize.id.asc())
        return render_template('summary.html', order=order, pizzas_in_cart=pizzas_in_cart)

    return render_template('cart_payment.html')

@bp.route('/cart/success', methods=['GET', 'POST'])
def success_payment():
    if request.method == 'POST':
        status = request.args.get('status')
        db.session.execute("DELETE FROM pizza_customize")
        if status == "OK":
            order = db.session.query(Order).order_by(Order.id.desc()).first()
            order.is_paid = 1
            db.session.add(order)
            db.session.commit()
            return render_template('success.html')
        else:
            db.session.execute("DELETE FROM pizza_customize")
            db.session.commit()
            return render_template('fail.html')
    else:
        return render_template('index.html')


@bp.route('/cart/delete/<int:page>', methods=['GET', 'POST'])
def cart_pizza_delete(page=0):
    entry = Pizza_customize.query.get_or_404(page)
    db.session.delete(entry)
    db.session.commit()

    pizzas_in_cart = Pizza_customize.query.order_by(
    Pizza_customize.id.asc()
    )
    return redirect(url_for('bp_cart.index_get'))
    #return render_template('cart.html', pizzas_in_cart=pizzas_in_cart)

@bp.route('/cart/summary', methods=['GET', 'POST'])
def cart_summary():
    return render_template('summary.html')