import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import contextily
import io
import pandas as pd
import pymssql
from flask import Flask, render_template, request, Response

app = Flask(__name__)

matplotlib.use('Agg')


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/selezione', methods=['GET'])
def selezione():
    global df1
    global df2
    scelta = request.args["scelta"]
    if scelta == "es1":

        conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',
                               user='riva.valentino', password='xxx123##', database='riva.valentino')
        # invio query al database e ricezione informazioni
        query = 'SELECT category_name, count(*) as numero_prodotti FROM production.products inner join production.categories on categories.category_id = products.category_id group by category_name'
        df1 = pd.read_sql(query, conn)
        return render_template("uno.html", nomiColonne=df1.columns.values, dati=list(df1.values.tolist()))

    elif scelta == "es2":
        conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',
                               user='riva.valentino', password='xxx123##', database='riva.valentino')
    # invio query al database e ricezione informazioni
        query = 'SELECT store_name, count(*) as numero_ordini from sales.orders inner join sales.stores on stores.store_id = orders.store_id group by store_name'
        df2 = pd.read_sql(query, conn)
        
        return render_template("due.html", nomiColonne=df2.columns.values, dati=list(df2.values.tolist()))
    elif scelta == "es3":
     return render_template("tre.html")
    elif scelta == "es4":
     return render_template("search.html")


@app.route("/graficoes1", methods=["GET"])
def graficoes1():
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.autofmt_xdate(rotation=90)
    ax.bar(df1.category_name, df1.numero_prodotti, color='g')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route("/graficoes2", methods=["GET"])
def graficoes2():
    fig = plt.figure()
    ax = plt.axes()
    fig.autofmt_xdate(rotation=0)
    ax.barh(df2.store_name, df2.numero_ordini, color='g')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/results', methods=['GET'])
def result():
    # collegamneto al database
    #import pandas as pd
    #import pymssql
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',
                           user='riva.valentino', password='xxx123##', database='riva.valentino')
    # invio query al database e ricezione informazioni
    nomeprodotto = request.args['NomeProdotto']
    query = f"select * from production.products where product_name like '{nomeprodotto}%'"
    dfprodotti = pd.read_sql(query, conn)
    # visualizzare le informazioni

    return render_template('result.html', nomiColonne=dfprodotti.columns.values, dati=list(dfprodotti.values.tolist()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
