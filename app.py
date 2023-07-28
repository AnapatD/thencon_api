import thencon
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return 'Server is up and running.<br>You can send us some requests!'

@app.route('/translate', methods=["GET"])
def run():
    method = request.form.get("method")
    text = request.form.get("text")
    if method.lower() == "th" or method.lower() == "ะ้" or method.lower() == "ธ็":
      method = 1
      return thencon.translate(method, text)
    elif method.lower() == "en" or method.lower() == "ำื" or method.lower() == "ฎ์":
      method = 2
      return thencon.translate(method, text)
    else:
      return "Please submit the valid method. (th/en)"