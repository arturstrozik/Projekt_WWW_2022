from flask import Blueprint, request, current_app, g, render_template, flash, redirect, url_for, jsonify
from sqlalchemy.exc import OperationalError


bp = Blueprint('bp_gallery', __name__)

@bp.route('/gallery', methods=['GET', 'POST'])
def index_get():
    return render_template('gallery.html')
