import pandas as pd
from flask import Flask, render_template, url_for, redirect, request

df = pd.DataFrame()

response = []

app = Flask(__name__)
app.secret_key = 'Shiro'

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/view')
def view():
    values = df.head(10).values.tolist()
    return render_template('view.html', labels=df.keys(), values=values)

@app.route('/load')
def load_dataFrame():
    global df
    df = pd.read_csv("static/exemple.csv")

    print("ok")

    return redirect(url_for('view'))

@app.route('/checknull')
def check_null():

    null_counts = df.isnull().sum().tolist()

    global response

    response = []

    for i, label in enumerate(df.keys()):
        response.append([label, null_counts[i]])

    return response

@app.route('/get_responce')
def get_responce():
    global response
    print(response)
    return render_template("responce.html", resp=response)

app.run(debug=True)