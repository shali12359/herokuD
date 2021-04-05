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

@app.route("/predictVerbal", methods=["POST"])
def predict():
    # GET AUDIO FILE & SAVE
    # audio = request.files['file']
    # fileName = str(random.randint(0, 100000))
    # audio.save(fileName)

    # INVOKE SPOTTING SYSTEM
    identify_voice = voice_identifying_service()

    # MAKE PREDICTION
    # predicted_number = identify_voice.predict(fileName)
    predicted_number = identify_voice.predict('222_1.wav')

    # # REMOVE AUDIO FILE
    # # os.remove(fileName)

    # # SEND BACK PREDICTION
    voice_dataset = {'Keyword': predicted_number}

    print(predicted_number)
    return jsonify(voice_dataset)

    # return "7"
	
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9696, debug=True)