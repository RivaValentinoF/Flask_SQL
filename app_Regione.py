from flask import Flask,render_template, request, Response, redirect, url_for
app = Flask(__name__)
import pymssql


@app.route('/', methods=['GET'])
def home():
    return render_template('home_Regioni.html')


@app.route('/selezione', methods=['GET'])
def selezione():
    global df1
    global df2
    global df3
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
         conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',
                               user='riva.valentino', password='xxx123##', database='riva.valentino')
        # invio query al database e ricezione informazioni
         query = 'SELECT brand_name, count(*) as numero_prodotti FROM production.products inner join production.brands on brands.brand_id = products.brand_id group by brand_name'
         df3 = pd.read_sql(query,conn)

         return render_template("tre.html", nomiColonne=df3.columns.values, dati=list(df3.values.tolist()))
    elif scelta == "es4":
        return render_template("search.html")
