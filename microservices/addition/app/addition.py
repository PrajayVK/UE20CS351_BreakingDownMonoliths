from flask import Flask, render_template, request, flash, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.secret_key = "secret_key"

@app.get("/<int:n1>&<int:n2>")
def add(n1, n2):
    return jsonify({"result":n1+n2})

if __name__=="__main__":
    app.run(debug=True, port=5051, host="0.0.0.0")