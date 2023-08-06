from flask import Flask,render_template,redirect,url_for

from tkinter import *
from PIL import ImageTk

app = Flask(__name__)


@app.route('/')
def landpage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



