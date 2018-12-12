import pandas as pd

def normalise(data, to, fro, imp):
    data[to] = ((data[fro] 
        - data[fro].mean()) 
        / (data[fro].max() 
        - data[fro].min()))*imp

def residential(params):
    # params = dict(povert: yes, )

    data_cols = ["geo_name","geo_id","pop","obesity","poverty",
    "high_school_graduation","unemployment","violent_crime","age","median_property_value"]
    data = pd.read_csv("../data/data_by_county.csv", sep=",", names=data_cols, encoding="latin-1")

    # weight data and return

    # normalise population
    data["pop"] = ((data["pop"] - data["pop"].mean()) 
        / (data["pop"].max() - data["pop"].min()))

    # make health entry
    data["health"] = data["obesity"] + data["violent_crime"]
    data["health"] = ((data["health"] - data["health"].mean()) 
        / (data["health"].max() - data["health"].min()))

    imp = 1
    # weighter. this decreases importance by .1 for each param
    for i in params.order():

        if params[i] == "education":
            data["high_school_graduation"] = data["high_school_graduation"]

            normalise(data, "education", "high_school_graduation", imp)

        elif params[i] == "jobs":

            # as we want lowest unemployment
            normalise(data, "employment", "unemployment", imp*-1)

        imp -= .1


    # for _,row in data.iterrows():
        
    #     print(row['health'])
        
    print(data["employment"].max())
    print(data["education"].max())
    print(params)

# residential("")

# def res_schema(params):
