
from flask import send_file
app = Flask(__name__)

@app.route('/')
def Weather_Ensembles():
    return '<h1>Weather Ensemble Demo</h1>'


@app.route('/temp1')
def get_temp1():
    return send_file('forecast temp1.png', mimetype='image/png')

@app.route('/temp2')
def get_temp2():
    return send_file('forecast temp2.png', mimetype='image/png')

  
@app.route('/wind1')
def get_wind1():
   return send_file('forecast wind1.png', mimetype='image/png')

@app.route('/wind2')
def get_wind2():
   return send_file('forecast wind2.png', mimetype='image/png')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
