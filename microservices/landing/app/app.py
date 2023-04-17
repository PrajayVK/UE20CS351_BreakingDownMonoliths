from flask import Flask, render_template, request, flash
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
app.secret_key = "secret_key"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first = request.form.get("first")
        second = request.form.get("second")
        operation = request.form.get("operation")
        
        # Fix variable type
        try:
            first = int(first)
            second = int(second)
        except (ValueError, TypeError):
            flash("Invalid input. Please enter valid integer values.")
            return render_template("index.html")

        # Handle None type exception
        if first is None or second is None:
            flash("Invalid input. Please enter valid integer values.")
            return render_template("index.html")
        
        result = 0
        if operation == "add":
            response = requests.get(f"http://addition:5051/{first}&{second}")
            data = response.json()
            result = data["result"]
        elif operation == "minus":
            result = first - second
        elif operation == "multiply":
            result = first * second
        elif operation == "divide":
            if second == 0:
                flash("Invalid input. Cannot divide by zero.")
                return render_template("index.html")
            result = first / second

        flash(f"The result of {operation} operation is {result}.")
        
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
