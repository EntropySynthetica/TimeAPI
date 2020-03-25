from flask import Flask
from flask import jsonify
import time
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return "Nothing to see here"

@app.route('/time')
def return_time():
    epoch_time = time.time()
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%dT%H:%M:%S.%f") + time.strftime("%z", time.localtime(epoch_time))
    day_of_week = int(now.strftime("%w"))
    day_of_year = int(now.strftime("%-j"))

    if time.localtime().tm_isdst == 1:
        dst = True
    else:
        dst = False

    time_dict = {
        'datetime' : date_time, 
        'unixtime' : epoch_time,
        'day_of_week' : day_of_week,
        'day_of_year' : day_of_year,
        'dst' : dst
        }

    return jsonify(time_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30180)