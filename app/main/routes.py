from flask import render_template

from app.main import bp


@bp.route('/')
def index():
    the_cards = [
        {'name': 'Humidity', 'value': 77, 'scale':'%','fg':'white','bg':'blue','bdr':'gray'},
        {'name': 'Temperature', 'value': 77, 'scale':"°C",'fg':'white','bg':'orange','bdr':'gray'},
        {'name': 'Pressure', 'value': 2134.5, 'scale': 'hPa','fg':'white','bg':'pink','bdr':'gray'},
    ]
    return render_template("index.html", cards=the_cards)


@bp.route('/test/')
def test_page():
    return '<h1>Testing the Flask Application Factory Pattern</h1>'
