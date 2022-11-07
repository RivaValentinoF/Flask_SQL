#Realizzare un sito web cyhe permetta di visualizzare tutti i dipendenti che lavorano in un certo store. 
# Il maneger inserisce il nome dello store e clicca su un bottone che invia i dati al server. 
# Quest'ultimo accede al database e restituisce i nomi e i cognomi dei dipendenti di quello store.
#  Se il nome dello store non è presente, deve essere restituito un opportuno messaggio di errore. 
# Tutta la parte grafica deve essere gestita con Bootstrap.

from flask import Flask, render_template, request, Response

import pandas as pd
import pymssql 
#pip install -U pip
#pip install pymssql

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home1.html')

@app.route('/ricerca', methods=['GET'])
def ricerca():
    NomeStore = request.args['NomeStore']
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',user='riva.valentino', password='xxx123##', database='riva.valentino')
    query = f"Select sf.first_name, sf.last_name, from sales.stores inner as st join sales.staffs as sf on sf.store_id =st.store_id where st.store_name=  '{NomeCliente}' "
    df = pd.read_sql(query, conn)
    
    return render_template('risultati1.html',nomiColonne=df.columns.values, dati=lis(df.values.tolist()))





if __name__ == '__main__':
 app.run(host='0.0.0.0', port=3245, debug=True)