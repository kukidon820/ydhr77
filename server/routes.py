from flask import Blueprint, render_template, request, redirect, url_for, flash
from data.create_engine import get_db
from data.models import GeoData
import json
from datetime import datetime

routes = Blueprint("routes", __name__)


@routes.route('/', methods=["GET", "POST"])
def upload_file():

    if request.method == 'POST':
        if "file" not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        try:
            data = json.load(file)
            for item in data:
                name = item['name']
                data_str = item['date']

                if not name or not data_str:
                    flash('There are no keys like "name" or "date" in file')
                    return redirect(request.url)

                if len(name) >= 50:
                    flash('key "name" is so long, not more than 50 characters')
                    return redirect(request.url)

                try:
                    date = datetime.strptime(data_str, '%Y-%m-%d_%H:%M')
                except ValueError:
                    flash('Invalid format for key "date"')
                    return redirect(request.url)

                geo_data = GeoData(name=name, date=date)
                with get_db() as db:
                    db.add(geo_data)
                    db.commit()

            flash('Data was uploaded successfully')
        except Exception as e:
            flash(f'Something went wrong {e}')

    return render_template('index.html')


@routes.route('/table', methods=["GET"])
def show_table():
    with get_db() as db:
        geo_data = db.query(GeoData).all()
    return render_template("table.html", records=geo_data)
