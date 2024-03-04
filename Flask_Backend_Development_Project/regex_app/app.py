from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)

    return render_template('home.html', matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    if re.match(r'^[\w\.-]+@[\w\.-]+$', email):
        validation_result = 'Valid email address.'
    else:
        validation_result = 'Invalid email address.'
    # Optionally, render a template for displaying validation results
    return render_template('home.html', validation_result=validation_result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
