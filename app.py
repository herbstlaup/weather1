
from flask import Flask
app = Flask(__name__)

@app.route('/')
def Weather_Ensembles():
    return '<h1>Hello, World ! - Pyflask Demo</h1>'

@app.route('/temp1')
def get_temp1():
    return '<h1>App version : <b>2.0</b></h1>'

@app.route('/temp2')
def get_temp2():
    return '<h1>You are accessing /test endpoint</h1>'

  
@app.route('/wind1')
def get_wind1():
  return '<h1>You are accessing /test endpoint</h1>'

@app.route('/wind2')
  def get_wind2():
  return '<h1>You are accessing /test endpoint</h1>'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
