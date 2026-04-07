from flask import Flask, render_template, request, redirect
from unicodedata import category

app = Flask(__name__)

LENGTH_UNITS = ['millimeter', 'centimeter', 'meter', 'kilometer', 'inch', 'foot', 'yard', 'mile']
WEIGHT_UNITS = ['milligram', 'gram', 'kilogram', 'ounce', 'pound']
TEMPERATURE_UNITS = ['Celsius', 'Fahrenheit', 'Kelvin']

def length_calculator(value, unit_from, unit_to):
    meter_length = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1.0,
        'kilometer': 1000.0,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34
    }

    shortcuts = {
        'millimeter': 'mm',
        'centimeter': 'cm',
        'meter': 'm',
        'kilometer': 'km',
        'inch': 'in',
        'foot': 'ft',
        'yard': 'yd',
        'mile': 'mi'
    }
    meters = value * meter_length[unit_from]
    result = meters / meter_length[unit_to]

    return f"{value} {shortcuts[unit_from]} = {round(result, 4)} {shortcuts[unit_to]}"

def weight_calculator(value, unit_from, unit_to):
    gram_weight = {
        'milligram': 0.001,
        'gram': 1.0,
        'kilogram': 1000.0,
        'ounce': 28.3495,
        'pound': 453.592
    }

    shortcuts = {
        'milligram': 'mg',
        'gram': 'g',
        'kilogram': 'kg',
        'ounce': 'oz',
        'pound': 'lb'
    }

    grams = value * gram_weight[unit_from]
    result = grams / gram_weight[unit_to]

    return f"{value} {shortcuts[unit_from]} = {round(result, 4)} {shortcuts[unit_to]}"

def temperature_calculator(value, unit_from, unit_to):
    shortcuts = {
        'Fahrenheit': '°F',
        'Kelvin': 'K',
        'Celsius': '°C',
    }

    if unit_from == 'Fahrenheit':
        celsius = (value - 32) * 5/9
    elif unit_from == 'Kelvin':
        celsius = value - 273.15
    else:
        celsius = value

    if unit_to == 'Fahrenheit':
        result = (celsius * 9/5) + 32
    elif unit_to == 'Kelvin':
        result = celsius + 273.15
    else:
        result = celsius

    return f"{value} {shortcuts[unit_from]} = {round(result, 2)} {shortcuts[unit_to]}"

@app.route('/')
def home():
    return redirect('/length')
@app.route('/length', methods=['GET','POST'])
def length():
    result = None
    if request.method == 'POST':
        input_value = float(request.form.get('value'))
        unit_from = request.form.get('unit_from')
        unit_to = request.form.get('unit_to')

        result = length_calculator(input_value, unit_from, unit_to)

        return render_template('index.html', category='length', units=LENGTH_UNITS, result=result)

    else:
        return  render_template('index.html', category='length', units=LENGTH_UNITS, result=None)
@app.route('/weight', methods=['GET','POST'])
def weight():
    if request.method == 'POST':
        input_value = float(request.form.get('value'))
        unit_from = request.form.get('unit_from')
        unit_to = request.form.get('unit_to')

        result = weight_calculator(input_value, unit_from, unit_to)

        return render_template('index.html', category='weight', units=WEIGHT_UNITS, result=result)

    else:
        return render_template('index.html', category='weight', units=WEIGHT_UNITS, result=None)
@app.route('/temperature', methods=['GET','POST'])
def temperature():
    if request.method == 'POST':
        input_value = float(request.form.get('value'))
        unit_from = request.form.get('unit_from')
        unit_to = request.form.get('unit_to')

        result = temperature_calculator(input_value, unit_from, unit_to)

        return render_template('index.html', category='temperature', units=TEMPERATURE_UNITS, result=result)

    else:
        return render_template('index.html', category='temperature', units=TEMPERATURE_UNITS, result=None)


if __name__ == "__main__":
    app.run(debug=True)


