"""
Routes and views for the flask application.
"""

from flask import Flask, render_template, request
import requests
import json
import re
from jinja2 import Template

app = Flask(__name__)
@app.route("/")

def home():

    question = request.args.get('question')
#   reco_type = request.args.get('Recommendation_types')

    if question is not None and question != "":
        # to remove special characters from question
        question = re.sub('[^A-Za-z0-9 ]+', '', question)
        result = requests.get('https://inpharmd.pythonanywhere.com/recommendation?' + 'question=' + str(question) + '&username=' + 'administrator' + '&password=' + 'inpharmD')
        print(result.text)
        parsed = json.loads(result.text)
        return render_template('home.html', parsed = parsed, question1=question)
    else:
        result = requests.get('https://inpharmd.pythonanywhere.com/recommendation?' + 'question=' + 'What are the quality tools in the pharmacy' + '&username=' + 'administrator' + '&password=' + 'inpharmD')
        print(result.text)
        parsed = json.loads(result.text)
        return render_template("home.html", parsed = parsed, question1=" ")

if __name__ == "__main__":
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)