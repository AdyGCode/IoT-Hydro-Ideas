from flask import render_template

from app.main import bp


@bp.route('/')
def index():
    the_cards = [
        {'name': 'Humidity', 'value': 77, 'scale':'%'},
        {'name': 'Temperature', 'value': 77, 'scale':"°C"},
        {'name': 'Pressure', 'value': 2134.5, 'scale': 'hPa'},
    ]
    return render_template("index.html", cards=the_cards)


@bp.route('/test/')
def test_page():
    return '<h1>Testing the Flask Application Factory Pattern</h1>'
