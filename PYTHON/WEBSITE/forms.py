from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField

from .models import Games

class GameSelectForm(FlaskForm):
    games = QuerySelectField('Games', query_factory=lambda: Games.query.all(), allow_blank=False, get_label='title')
    