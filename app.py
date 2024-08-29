from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=["get","post"])
def index():
    return render_template('index.html')

@app.route('/store_money',methods=["get","post"])
def store_money():
    return render_template('store_money.html')

@app.route('/transfer_money',methods=["get","post"])
def transfer_money():
    return render_template('transfer_money.html')

if __name__=='__main__':
    app.run()
