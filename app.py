import flask
from flask import jsonify
from test import sayHello

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def predict():
  sayHello('Shalitha')
  return jsonify({ 'msg': 'Hello Android'})

@app.route('/predict', methods = ['GET', 'POST'])
def predictNew():
  sayHello('Shalitha')
  return jsonify({ 'msg': 'Hello Android 2'})
	
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9696, debug=True)