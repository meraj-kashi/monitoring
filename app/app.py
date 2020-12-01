import time
import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
PrometheusMetrics(app)



@app.route('/store1')
def first_route():
    time.sleep(random.random() * 1000)
    return 'store-1', 100


@app.route('/store2')
def the_second():
    time.sleep(random.random() * 1000)
    return 'store-2'


@app.route('/store3')
def test_3rd():
    time.sleep(random.random() * 1000)
    return 'store-3', 300


@app.route('/store4')
def fourth_one():
    time.sleep(random.random() * 1000)
    return 'store-4', 400


@app.route('/store5')
def fith_one():
    time.sleep(random.random()*1000)
    return 'store-5', 500


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
