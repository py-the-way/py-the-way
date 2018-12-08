import pandas as pd

def residential(params):
    # params = dict(povert: yes, )

    data_cols = ["geo_name","geo_id","poverty"]
    data = pd.read_csv("../../data/test1.csv", sep=",", names=data_cols, encoding="latin-1")

    print(data)

residential("")
