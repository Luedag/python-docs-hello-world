## Libraries are imported

from flask import Flask

import pandas as pd

import time

import numpy as np

import json

import networkx as nx

from flask import request, jsonify

airport_data = pd.read_csv("airport_data.csv")

airport_graph = nx.from_pandas_edgelist(df = airport_data, source = "location_1", target = "location_2")

app = Flask(__name__)

@app.route("/")
def airportRouter():
    #return "Airport API in construction"

    taxi_origin = request.args['taxi_origin']

    taxi_destination = request.args['taxi_destination'] 
    
    main_output = nx.shortest_path(airport_graph, source = taxi_origin, target = taxi_destination)

    output_dict = {}

    output_dict["origin"] = main_output[0]

    output_dict["destination"] = main_output[-1]

    del main_output[0]

    del main_output[-1]

    output_dict["Taxiways"] = []

    for i in main_output:

        output_dict["Taxiways"].append({"Way" : i})

    #print(main_output)
           
    return jsonify(output_dict)