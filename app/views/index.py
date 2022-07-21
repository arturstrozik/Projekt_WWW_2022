from flask import Blueprint, request, current_app, g, render_template, flash, redirect, url_for, jsonify


bp = Blueprint('bp_index', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index_get():
    return render_template('index.html')
