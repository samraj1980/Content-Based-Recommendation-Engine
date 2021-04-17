"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import inpharmd_recommend_web_app.views
