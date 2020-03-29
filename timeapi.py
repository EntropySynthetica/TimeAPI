from flask import Flask
from flask import jsonify
import time
from datetime import datetime
import pytz

app = Flask(__name__)

def is_dst(time, timezone):
    if time is None:
        time = datetime.utcnow()
    timezone = pytz.timezone(timezone)
    timezone_aware_date = timezone.localize(time, is_dst=None)
    return timezone_aware_date.tzinfo._dst.seconds != 0


@app.route('/')
def hello():
    return "Nothing to see here"

@app.route('/time')
def return_time_utc():
    epoch_time = time.time()
    time_zone_str = 'etc/utc'
    time_zone = pytz.timezone(time_zone_str)
    now = datetime.utcnow()
    date_time = now.strftime("%Y-%m-%dT%H:%M:%S.%f") + "+00:00"
    day_of_week = int(now.strftime("%w"))
    day_of_year = int(now.strftime("%-j"))

    dst = False

    time_dict = {
        'datetime' : date_time, 
        'unixtime' : epoch_time,
        'day_of_week' : day_of_week,
        'day_of_year' : day_of_year,
        'time_zone' : time_zone_str,
        'dst' : dst,
        'abbreviation' : "UTC"
        }

    return jsonify(time_dict)

@app.route('/time/<time_zone_area>/<time_zone_location>')
def return_time_tz(time_zone_area, time_zone_location):
    epoch_time = time.time()
    time_zone_str = time_zone_area + "/" + time_zone_location

    try:
        time_zone = pytz.timezone(time_zone_str)
        now = datetime.now(time_zone)
        date_time = now.strftime("%Y-%m-%dT%H:%M:%S.%f") + now.strftime("%z")
        day_of_week = int(now.strftime("%w"))
        day_of_year = int(now.strftime("%-j"))

        dst = is_dst(datetime.now(), time_zone_str)

        time_dict = {
            'datetime' : date_time, 
            'unixtime' : epoch_time,
            'day_of_week' : day_of_week,
            'day_of_year' : day_of_year,
            'time_zone' : time_zone_str,
            'dst' : dst,
            'abbreviation' : now.strftime("%Z")
            }

        return jsonify(time_dict)
    except Exception as error:
        error_dict = {'error' : str(type(error))}
        return jsonify(error_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)