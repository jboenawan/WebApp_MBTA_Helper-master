"""
Simple "Hello, World" application using Flask
"""

from flask import Flask
from flask import render_template
from flask import request

from mbta_helper import find_stop_near

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        place_name = request.form['place_name']
        stop, distance, first_time = find_stop_near(place_name)
        return render_template('result.html', stop= stop, distance=distance, first_time=first_time)
    else:
        return render_template('index.html', error=None)



if __name__ == '__main__':
    app.run()
