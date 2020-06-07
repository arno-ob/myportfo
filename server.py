from flask import Flask, render_template, request, url_for
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return 'Coming soon!'


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        name = data["contactName"]
        email = data["contactEmail"]
        subject = data["contactSubject"]
        message = data["contactMessage"]

        csv_writer = csv.writer(
            database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return 'Your message was sent. Thank you. '
    else:
        return 'Something went wrong'
