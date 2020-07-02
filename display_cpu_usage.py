""" Display or graph the control_fan.py log file """

from datetime import datetime
import logging # So we can change the log level

# import flask
from flask import Flask, render_template, request

import psutil

VERSION = "1.0.1"

# To prevent Flask from logging each "GET" to console, change the log level to ERROR
# for 'werkzeug' (Flask).
# 2020-06=04; From https://stackoverflow.com/a/18379764/641450
log = logging.getLogger('werkzeug') # pylint: disable=invalid-name
log.setLevel(logging.ERROR)

app = Flask(__name__) # pylint: disable=invalid-name
#app.debug = True # Uncomment to debug


@app.route('/')
def home():
    """ Display the current CPU usage """
    
    template_values = {
        'VERSION' : VERSION,
        'cpu_percent' : psutil.cpu_percent(),
        'current_datetime_str' : datetime.now().strftime("%H:%M:%S on %a %d %b %Y")
    }
    
    return render_template('display_cpu_usage.html.j2', **template_values)
    
    return str(psutil.cpu_percent()) + '%'


if __name__ == '__main__':
    print(f"Starting v{VERSION}")
    app.run(debug=False, host='0.0.0.0', port=8088)
