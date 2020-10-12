import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def Home():
	return (
		f"Available Routes:<br>"
		f"/api/v1.0/precipitation<br>"
		f"/api/v1.0/stations<br>"
		f"/api/v1.0/tobs<br>"
		f"/api/v1.0/<start><br>"
		f"/api/v1.0<start>/<end><br>"
		)


@app.route("/api/v1.0/precipitation")
def precipitation():

	prcp = session.query(Measurement.date, Measurement.tobs)\
    		.filter(Measurement.date.between('2016-08-23', '2017-08-23').\
		order_by(Measurement.date).all()

  precipitation_data = []
    for p in prcp:
        prcp_values = {}
        prcp_values["date"] = p.date
        prcp_values["precipitation"] = p.precipitation
        precipitation_data.append(prcp_values)

    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
	  stations_data = session.querysession.query(Measurement.date, Measurement.tobs).\
        .filter(Measurement.date.between('2016-08-23', '2017-08-23').all()
	
    return jsonify(stations_data)

@app.route("/api/v1.0/tobs")
def tobs():


@app.route("/api/v1.0/<start>")
def start(start):


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):



if __name__ == "__main__":
    app.run(debug=True)