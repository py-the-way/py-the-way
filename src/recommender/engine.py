import pandas as pd
def res_choose(data, params, top):

    data["order"]["order"] = data["order"]["education"] + data["order"]["employment"] + data["order"]["health"]

    # index = order.idxmax()
    order = data["order"].sort_values("order", ascending=False)

    i = 0

    order_top = []
    for _, row in order.iterrows():

        # find best order
        if i < 30:
            order_top.append(row)
        i += 1

    
    # prefs

    prefs = data["prefs"]
    for i, row in enumerate(order_top):

        index = row.name

        if prefs.iloc[index]["geo_id"] == row["geo_id"]:
            order_top[i]["prefs"] = (prefs.iloc[index]["pop"] 
                + prefs.iloc[index]["price"])

    # sort by prefs (lower the better)
    order_top = sorted(order_top, key=lambda k: k["prefs"])
    
    return pd.DataFrame(order_top[:top])