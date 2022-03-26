import base64
from io import BytesIO
from flask import Flask
from flask import render_template
from matplotlib.figure import Figure
import pandas as pd
import sqlite3
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect(database='database/main.db')

    variables1 = pd.read_sql('SELECT * FROM temp', conn)
    variables2 = pd.read_sql('SELECT * FROM drugs', conn)

    temp =variables1['T']
    drugs =variables2['D']

    tempRead = np.array(temp)
    drugsRead = np.array(drugs)
    
    #Graf 1
    fig1 = Figure(figsize=(15, 6))
    ax1 = fig1.subplots()
    ax1.plot(tempRead, linestyle = 'solid', c = '#76538E', linewidth = '1', marker = 'o', mec = '#76538E', ms = 10, mfc = 'white')
    ax1.set_facecolor("#e0e0e0")
    fig1.patch.set_facecolor('#e0e0e0')
    ax1.set_title("Temperatur")
    buf = BytesIO()
    fig1.savefig(buf, format="png")
    dataTemp = base64.b64encode(buf.getbuffer()).decode("ascii")
    #Graf2
    fig2 = Figure(figsize=(15, 6))
    ax2 = fig2.subplots()
    ax2.plot(drugsRead, linestyle = 'solid', c = '#76538E', linewidth = '1', marker = 'o', mec = '#76538E', ms = 10, mfc = 'white')
    ax2.set_facecolor("#e0e0e0")
    fig2.patch.set_facecolor('#e0e0e0')
    ax2.set_title("Næringsstoffer")
    buf = BytesIO()
    fig2.savefig(buf, format="png")
    dataDrug = base64.b64encode(buf.getbuffer()).decode("ascii")
    #Website
    return render_template("index.html", grafDataTemp=dataTemp, grafDataDrug=dataDrug)

if __name__ == '__main__':
    app.run()


"""
<img src='data:image/png;base64,{{ grafData }}'>

<script type=text/javascript src="{{
        url_for('static', filename='pictureChange.js') }}"></script>

<div>
                    <img src='data:image/png;base64,{{ grafDataTemp }}' class="center" style="width: 100%;">
                    <img src='data:image/png;base64,{{ grafDataDrug }}' class="center" style="width: 100%;">
                </div>
"""