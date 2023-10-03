import pandas as pd
from flask import Flask, render_template, url_for, redirect, request
import io


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
def load_dataFrame(url_file: str = None):
    global df

    if df.empty:
        df = pd.read_csv("static/files_data/exemple.csv")

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
    return render_template("null_values_view.html", resp=response)

@app.route('/drop_column')
def drop_column():
    global df

    df = df.drop(columns=df.columns[0])
    return redirect(url_for('view'))

@app.route('/describe')
def describe():
    global df

    descricao = df.describe()
    columns = descricao.keys()
    rows = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
    return render_template("describe_view.html", desc=descricao.values.tolist(), columns=columns, rows=rows)

@app.route('/info')
def info():
    global df

    buffer = io.StringIO()

    df.info(buf=buffer)
    return render_template("info_view.html", values=buffer.getvalue().split('\n'))

@app.route('/upload_file', methods=['post', ])
def upload_file():
    global df
    file = request.files['file']
    url = "static/files_data" + file.filename
    file.save(url)
    df = pd.read_csv(url)
    return redirect(url_for('view'))

app.run(debug=True)


