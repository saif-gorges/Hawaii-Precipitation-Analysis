import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Sqlalchemy

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#Flask
app = Flask(__name__)

@app.route("/")
def index():
    return(
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    session.close()
    precipitation_data = session.query(Measurement).filter(Measurement.date >= '2016-08-20')
    precipitation_df = pd.read_sql_query(precipitation_data.statement, session.bind)
    precipitation_df_final = precipitation_df[["date", "prcp"]].set_index("date")
    return jsonify(precipitation_df_final.to_dict())

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    sel = [Measurement.station, func.count(Measurement.station), Station.name]
    stations = session.query(*sel).filter(Station.station == Measurement.station).group_by(Measurement.station).all()
    session.close()
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    active_station = 'USC00519281'
    station_1 = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == active_station).all()
    return jsonify(station_1)

@app.route("/api/v1.0/<start>")
def Single(start):
    session = Session(engine)
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    single_date = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))
    session.close()
    trip = list(np.ravel(single_date))
    return jsonify(trip)

@app.route("/api/v1.0/<start>/<end>")
def Return(start, end):
    session = Session(engine)
    start_date = dt.datetime.strptime(start, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end, '%Y-%m-%d')
    return_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))
    travel = list(np.ravel(return_data))
    return jsonify(travel)

if __name__ == '__main__':
    app.run(debug = True)

