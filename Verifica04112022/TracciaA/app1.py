from flask import Flask, render_template, request, Response
app = Flask(__name__)

import io
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import pymssql

conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',
                           user='riva.valentino', password='xxx123##', database='riva.valentino')

@app.route("/", methods=["GET"])
def home():
    return render_template("home1.html")

@app.route("/ricerca", methods=["GET"])
def ricerca():
    nomeStore = request.args["NomeStore"]
    query = f"SELECT sf.first_name, sf.last_name FROM sales.stores as st INNER JOIN sales.staffs as sf ON st.store_id = sf.store_id WHERE st.store_name = '{nomeStore}'"
    tabella = pd.read_sql(query,conn)
    print(tabella)
    if tabella.values.tolist() == []:
        return render_template("error.html")
    else:
        return render_template("risultati1.html", nomiColonne = tabella.columns.values, dati = tabella.values)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)