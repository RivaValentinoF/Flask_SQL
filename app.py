from flask import Flask, render_template, request
app= Flask(__name__)

import io
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

@app.route('/', methods=['GET'])
def home():
     return render_template('home.html')

@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["scelta"]
    if scelta=="es1":
        return render_template("uno.html")
    elif scelta=="es2":
        return render_template("due.html")
    elif scelta=="es3":
        return render_template("tre.html")
    elif scelta=="es4":
        return render_template("search.html")

@app.route('/uno', methods=['GET'])
def es1(): 
    import pandas as pd
    import pymssql
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',
                           user='riva.valentino', password='xxx123##', database='riva.valentino')
    # invio query al database e ricezione informazioni
    query = 'SELECT category_name, count(*) as numero_prodotti FROM production.products inner join production.categories on categories.category_id = products.category_id group by category_name'
    dfprodotti = pd.read_sql(query, conn)



@app.route('/results', methods=['GET'])
def result():
    # collegamneto al database
    import pandas as pd
    import pymssql
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',
                           user='riva.valentino', password='xxx123##', database='riva.valentino')
    # invio query al database e ricezione informazioni
    nomeprodotto = request.args['NomeProdotto']
    query = f"select * from production.products where product_name like '{nomeprodotto}%'"
    dfprodotti = pd.read_sql(query, conn)
    # visualizzare le informazioni
   
    return render_template('result.html', nomiColonne = dfprodotti.columns.values, dati = list(dfprodotti.values.tolist()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
