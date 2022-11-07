from flask import Flask, render_template, request
import pandas as pd
import pymssql

app = Flask(__name__)




@app.route('/infoUser', methods=['GET'])
def infoUser():
    return render_template('infoUser.html')

@app.route('/results', methods=['GET'])
def result():
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS',
                           user='riva.valentino', password='xxx123##', database='riva.valentino')
    # invio query al database e ricezione informazioni
    NomeCliente = request.args['NomeCliente']
    CognomeCliente = request.args['CognomeCliente']
    
    query = f"select * from sales.customers where first_name = '{NomeCliente}'and last_name ='{CognomeCliente}'"
    df = pd.read_sql(query, conn)
    
    
    # visualizzare le informazioni
    dati=list(df.values.tolist())
    if dati == []:
      return render_template('errore.html')
    else:
     return render_template('result.html', nomiColonne=df.columns.values, dati=list(df.values.tolist()))
    






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
