import flask
from flask import jsonify
from test import sayHello
# from Voice_identifying_service import voice_identifying_service

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def predict():
  sayHello('Shalitha')
  return jsonify({ 'msg': 'Hello Android'})

@app.route('/predict', methods = ['GET', 'POST'])
def predictNew():
  sayHello('Shalitha')
  return jsonify({ 'msg': 'Hello Android 2'})

# @app.route('/predictVerbal', methods= ['GET', 'POST'])
# def predictVerbal():
#   identify_voice = voice_identifying_service()

#   predicted_number = identify_voice.predict('635_225.wav')

#   voice_dataset = {'Keyword': predicted_number}

#   return jsonify(voice_dataset)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9696, debug=True)
