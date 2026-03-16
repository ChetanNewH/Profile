from flask import Flask, render_template, url_for, redirect
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import os
import re

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/aboutCodroidhub')
def aboutCodroid():
    return render_template('aboutCodroidhub.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/web_scraping')
def web_scraping():
    return render_template('web_scraping.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000, host="0.0.0.0")