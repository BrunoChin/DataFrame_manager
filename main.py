import pandas as pd
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/view')
def view():
    df = load_dataFrame()
    values = df.head(10).values.tolist()
    return render_template('view.html', labels=df.keys(), values=values)

def load_dataFrame():
    df = pd.read_csv("static/exemple.csv")

    return df

app.run(debug=True)