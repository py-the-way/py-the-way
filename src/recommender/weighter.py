import pandas as pd

# TODO fix population

def normalise(data, to, fro, imp):
    data[to] = ((data[fro] 
        - data[fro].mean()) 
        / (data[fro].max() 
        - data[fro].min()))*imp

def residential(params):
    # First we do it county by county
    data_cols = ["geo_name","geo_id","pop","obesity","poverty",
    "high_school_graduation","unemployment","violent_crime","age","median_property_value"]
    data = pd.read_csv("../data/data_by_county.csv", sep=",", names=data_cols, encoding="latin-1")

    # weight data and return

    imp = 1
    # weighter. this decreases importance by .1 for each param
    for i in params.order():

        # make sure best option is highest

        if params[i] == "education":

            data["high_school_graduation"] = data["high_school_graduation"]

            normalise(data, "education", "high_school_graduation", imp)

            # TODO get college grads

        elif params[i] == "jobs":

            # as we want lowest unemployment
            normalise(data, "employment", "unemployment", imp*-1)

        elif params[i] == "health":

            # as violent crimes is per 100,000
            data["health"] = data["obesity"] + (data["violent_crime"] / 100000)

            normalise(data, "health", "health", imp*-1)

        # TODO THOMAS: finish this

        imp -= .1


    for k in params.prefs.keys():

        # the best is closest to 0 for these

        if k == "pop":

            data["pop"] = abs(params.prefs[k] - data["pop"])

        elif k == "price":

            data["price"] = abs(params.prefs[k] - data["median_property_value"])

        elif k == "urban":

            # TODO https://datausa.io/map/?level=county&key=population_living_in_a_rural_area&translate=761.5467090684273,1127.085723711873&scale=7082.5387813829975
            print(k)
        elif k == "industry":

            # TODO: get a certain number of industries here
            print(k)


    # TODO get states info

    print(params)

    return {
        "order": data[["geo_name", "geo_id", "education", "employment", "health"]],
        "prefs": data[["geo_name", "geo_id", "pop", "price"]]
    }
