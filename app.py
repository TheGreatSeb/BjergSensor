import base64
from io import BytesIO
from flask import Flask
from flask import render_template
from matplotlib.figure import Figure
import pandas as pd
import sqlite3
import numpy as np

app = Flask(__name__)
conn = sqlite3.connect(database='database/test.db')

variables1 = pd.read_sql('SELECT * FROM temp', conn)
variables2 = pd.read_sql('SELECT * FROM drugs', conn)

temp =variables1['T']
drugs =variables2['D']

tempRead = np.array(temp)
drugsRead = np.array(drugs)

@app.route("/")
def home():
    fig = Figure(figsize=(15, 6))
    ax = fig.subplots()
    ax.plot(tempRead, linestyle = 'solid', c = '#76538E', linewidth = '1', marker = 'o', mec = '#76538E', ms = 10, mfc = 'white', label='Temperatur')
    ax.plot(drugsRead, linestyle = 'solid', c = 'green', linewidth = '1', marker = 'o', mec = 'green', ms = 10, mfc = 'white', label='Næringsstoffer')
    ax.set_facecolor("#e0e0e0")
    fig.patch.set_facecolor('#e0e0e0')
    ax.set_title("Her er en god titel")
    ax.legend();
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")

    return render_template("index.html", grafData=data)

if __name__ == '__main__':
    app.run()


"""
<img src='data:image/png;base64,{{ grafData }}'>
"""