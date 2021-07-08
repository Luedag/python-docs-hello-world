## Libraries are imported

from flask import Flask

import pandas as pd

import time

import numpy as np

import json

from server import app

import networkx as nx

from flask import request, jsonify

airport_data = pd.read_csv("airport_data.csv")

airport_graph = nx.from_pandas_edgelist(df = airport_data, source = "location_1", target = "location_2")

app = Flask(__name__)

@app.route("/")
def hello():
    return "Airport API in construction"