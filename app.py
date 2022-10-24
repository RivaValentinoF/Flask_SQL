from flask import Flask,render_template, request

@app.route('/', methods=['GET']) 
def home():
    return render_template('search.html')

@app.route('/result', methods=['GET']) 
def result():
    #collegamneto al database 
    import pandas as pd
    import pymssql
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user= 'riva.valentino', password='xxx123##', database='riva.valentino')
    #invio query al database e ricezione informazioni 
    nomeprodotto=request.args['NomeProdotto']
    query= f"select * from production.products where products_name like '{NomeProdotto}%'"
    #visualizzare le informazioni 
    

    return render_template('search.html')

    



       
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)