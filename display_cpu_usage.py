""" Display or graph the control_fan.py log file """

from datetime import datetime

# import flask
from flask import Flask, render_template, request

import psutil

app = Flask(__name__)
#app.debug = True # Uncomment to debug

VERSION = "1.0.0"

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
