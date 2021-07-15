import json
import pandas as pd

alias_df = pd.read_csv("./location_alias.csv")

alias_dict = {}

for index, row in alias_df.iterrows():

    alias_dict[str(row["alias"])] = str(row["official_location_name"])

with open("./alias_dict.json", "w") as wf:
    json.dump(alias_dict, wf)