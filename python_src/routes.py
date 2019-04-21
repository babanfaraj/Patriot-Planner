from python_src import app
from flask import render_template, request
from python_src.models import Location, Building


@app.route('/')
@app.route('/index')
@app.route('/login')
def index():
    return render_template("index.html")


@app.route('/home', methods=['GET'])
def home():
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    print(all_building_names)
    return render_template("home.html", all_building_names=all_building_names)


@app.route('/new_route', methods=['GET'])
def new_route():
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    print(all_building_names)
    return render_template("new_route.html", all_building_names=all_building_names)


@app.route('/edit_schedule', methods=['GET'])
def edit_schedule():
    all_buildings = Building.query.all()
    all_building_names = [_.building_name for _ in all_buildings]
    print(all_building_names)
    return render_template("edit_schedule.html", all_building_names=all_building_names)


@app.route('/settings')
def settings():
    return render_template("settings.html")

