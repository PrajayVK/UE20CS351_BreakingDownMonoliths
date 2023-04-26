from flask import Flask, render_template, request, flash, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

def add(n1, n2):
    URL = 'http://addition-service:'
    port = 5051
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    try:
        response = requests.get(add_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f'Error occurred during addition: {str(e)}'
    return response.json()['result']

def minus(n1, n2):
    URL = 'http://subtraction-service:'
    port = 5052
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    try:
        response = requests.get(add_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f'Error occurred during subtraction: {str(e)}'
    return response.json()['result']

def multiply(n1, n2):
    URL = 'http://multiplication-service:'
    port = 5053
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    try:
        response = requests.get(add_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f'Error occurred during multiplication: {str(e)}'
    return response.json()['result']

def divide(n1, n2):
    URL = 'http://division-service:'
    port = 5054
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    try:
        response = requests.get(add_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f'Error occurred during division: {str(e)}'
    return response.json()['result']

def greater_than(n1, n2):
    URL = 'http://greater_than-service:'
    port = 5055
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    try:
        response = requests.get(add_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f'Error occurred during comparison: {str(e)}'
    return response.json()['result']

def less_than(n1, n2):
    URL = 'http://less_than-service:'
    port = 5056
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    try:
        response = requests.get(add_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f'Error occurred during comparison: {str(e)}'
    return response.json()['result']

def equal(n1, n2):
    URL = 'http://equal-service:'
    port = 5057
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    if response.status_code != 200:
        raise Exception('Error occurred during comparison')
    return response.json()['result']

@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        number_1 = float(request.form.get("first"))
        number_2 = float(request.form.get('second'))
        operation = request.form.get('operation')
        result = 0
        if operation == 'add':
            result = add(number_1, number_2)
        elif operation == 'minus':
            result =  minus(number_1, number_2)
        elif operation == 'multiply':
            result = multiply(number_1, number_2)
        elif operation == 'divide':
            if number_2==0:
                result = 'Zero Division Error'
            else:
                result = divide(number_1, number_2)
        elif operation == 'greater_than':
            result = greater_than(number_1, number_2)
        elif operation == 'less_than':
            result = less_than(number_1, number_2)
        elif operation == 'equal':
            result = equal(number_1, number_2)
        if result != "Zero Division Error":
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
        # Pass the result message to the template
    except:
        flash(f"Invalid Input")
    else:
        if result == 'Zero Division Error':
            flash("Zero Division Error")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )