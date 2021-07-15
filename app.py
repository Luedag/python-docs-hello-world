## Libraries are imported

from flask import Flask

import pandas as pd

import time

import numpy as np

import json

import networkx as nx

from flask import request, jsonify

airport_data = pd.read_csv("airport_data.csv")

with open("alias_dict.json", "r") as lf:
    alias_dict = json.load(lf)

airport_graph = nx.from_pandas_edgelist(df = airport_data, source = "location_1", target = "location_2")

app = Flask(__name__)

@app.route("/")
def airportRouter():
    #return "Airport API in construction"

    taxi_origin = request.args['taxi_origin']

    taxi_destination = request.args['taxi_destination']

    location_found = 0

    taxi_origin = taxi_origin.lower()

    try:

        taxi_origin = alias_dict[taxi_origin]

        location_found = 1

    except:

        location_found = 0
        
    try:

        main_output = nx.shortest_path(airport_graph, source = taxi_origin, target = taxi_destination)

        location_found = 1

    except:

        location_found = 0

    output_dict = {}

    if location_found == 1:

        output_dict["origin"] = main_output[0]

        output_dict["destination"] = main_output[-1]

        del main_output[0]

        del main_output[-1]

        output_dict["Taxiways"] = []

        for i in main_output:

            output_dict["Taxiways"].append({"Way" : i})

    else:

        output_dict["origin"] = "not_found"

        output_dict["destination"] = "not_found"

        output_dict["Taxiways"] = []

        output_dict["Taxiways"].append({"Way" : "not_found"})

    #print(main_output)
           
    return jsonify(output_dict)