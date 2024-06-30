from flask import Flask, render_template, request

app = Flask(__name__)


def convert_to_metric(value, unit):
    if unit == 'inches':
        return value * 2.54  # Convert inches to centimeters
    elif unit == 'feet':
        return value * 0.3048  # Convert feet to meters
    elif unit == 'yards':
        return value * 0.9144  # Convert yards to meters
    elif unit == 'miles':
        return value * 1.60934  # Convert miles to kilometers
    else:
        return None  # Invalid unit


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = float(request.form['value'])
        unit = request.form['unit']
        converted_value = convert_to_metric(value, unit)

        if converted_value is not None:
            if unit == 'inches':
                metric_unit = "centimeters"
            elif unit == 'feet':
                metric_unit = "meters"
            elif unit == 'yards':
                metric_unit = "meters"
            elif unit == 'miles':
                metric_unit = "kilometers"
            return render_template('result.html', value=value, unit=unit, converted_value=converted_value, metric_unit=metric_unit)
        else:
            error_message = "Invalid unit provided."
            return render_template('index.html', error_message=error_message)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
