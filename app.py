from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

#Reading data
##data_df = pd.read_csv("static/data/customers.csv")
##demography_df = data_df[(data_df['demography']=="Yes").notnull()]

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
   
