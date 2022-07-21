from flask import Blueprint, request, current_app, g, render_template, flash, redirect, url_for, jsonify
from flask_security import current_user, login_required
from sqlalchemy.exc import OperationalError

from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length

from ..app import db
from ..models import Opinion

bp = Blueprint('bp_opinion', __name__)


@bp.route('/opinion', methods=['GET'])
@bp.route('/opinion/page/<int:page>', methods=['GET'])
def opinion_get(page=1):
    entries = Opinion.query.order_by(
        Opinion.id.desc()
    ).paginate(page=page, per_page=current_app.config['PAGINATION_PER_PAGE'])

    is_null = db.session.execute("SELECT * FROM opinion")
    counter = 0
    for result in is_null:
        counter += 1

    return render_template('opinion.html', entries=entries, is_null=counter)


@bp.route('/opinion/add', methods=['GET', 'POST'])
def opinion_add_get_post():
    class OpinionAddForm(FlaskForm):
        name = TextAreaField('Nick', validators=[DataRequired(), Length(min=0, max=25)])
        message = TextAreaField('Twoja Opinia', validators=[DataRequired(), Length(min=0)])
        
    form = OpinionAddForm()

    if form.validate_on_submit():
        obj = Opinion(message=form.message.data, user_name=form.name.data)
        db.session.add(obj)
        db.session.commit()
        flash('The entry has been added.')
        return redirect(url_for('bp_opinion.opinion_get'))
    elif form.is_submitted():
        for field_name, errors in form.errors.items():
            for err in errors:
                flash(f"{form._fields[field_name].label.text}: {err}", 'error')

    return render_template('opinion_add.html', form=form)
