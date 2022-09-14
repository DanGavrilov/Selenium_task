from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from database import save_to_db, get_from_db
from flask import Flask, render_template
from parse import parse_html
import json

app = Flask(__name__)


@app.route('/')
def index():
    with open('data.json') as f:
        elements = json.load(f)

    return render_template('index.html', elements=elements)


if __name__ == '__main__':
    app.run()




