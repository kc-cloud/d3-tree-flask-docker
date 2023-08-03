from flask import Flask, jsonify, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

#Reading data
##data_df = pd.read_csv("static/data/customers.csv")
##demography_df = data_df[(data_df['demography']=="Yes").notnull()]
es_data = [
  {
    "name": "nexus",
    "parent": "null",
    "children": [
      {
        "name": "dev",
        "parent": "nexus",
        "children": [
          {
            "name": "service-1",
            "parent": "dev",

            "children": [
              {
                "name": "mysql-db",
                "parent": "service-1"
              },
              {
                "name": "s3",
                "parent": "service-1"
              }
            ]
                      
          },
          {
            "name": "service-2",
            "parent": "dev"
          }
        ]
      },
      {
        "name": "test",
        "parent": "nexus",
        "children": [
          {
            "name": "service-3",
            "parent": "test"
          },
          {
            "name": "service-4",
            "parent": "test"
          }
        ]
      }
    ]
  }
]

@app.route('/')
def index():
   return render_template('index.html', data = es_data)

if __name__ == '__main__':
    app.run(debug=True)
   
