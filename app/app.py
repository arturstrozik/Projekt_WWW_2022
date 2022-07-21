import os
import sys
from flask import Flask, render_template, redirect, url_for, request, session
from werkzeug.debug import DebuggedApplication
from flask_sqlalchemy import SQLAlchemy
from .config import STATIC_FOLDER

db = SQLAlchemy()

def create_app():
    app = Flask(__name__,
                instance_relative_config=False,
                static_folder=STATIC_FOLDER,
                static_url_path='/static'
                )

    app.config.from_pyfile('config.py')
    app.debug = True
    app.wsgi_app = DebuggedApplication(app.wsgi_app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config['SQLALCHEMY_DATABASE_URI'] = (f"mysql://{app.config['DB_USER']}:{app.config['DB_PASSWORD']}"
                                             f"@{app.config['DB_HOST']}/{app.config['DB_NAME']}")
    db.init_app(app)

    from .models import Order, Pizza, Pizza_customize, Opinion

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    from .views.index import bp as bp_index
    app.register_blueprint(bp_index)

    from .views.menu import bp as bp_menu
    app.register_blueprint(bp_menu)

    from .views.contact import bp as bp_contact
    app.register_blueprint(bp_contact)

    from .views.cart import bp as bp_cart
    app.register_blueprint(bp_cart)

    from .views.gallery import bp as bp_gallery
    app.register_blueprint(bp_gallery)

    from .views.opinion import bp as bp_opinion
    app.register_blueprint(bp_opinion)

    return app
