import pandas as pd

def residential(params):
    # params = dict(povert: yes, )

    data_cols = ["geo_name","geo_id","pop_2016","adult_obesity_2017","poverty_rate_2016",
    "high_school_graduation_2017","unemployment_2017","violent_crime_2017","age","median_property_value_2016"]
    data = pd.read_csv("../data/data_by_county.csv", sep=",", names=data_cols, encoding="latin-1")

    # weight data and return

    for _,row in data.iterrows():
        print(row['geo_name'])
        
    print(params)

# residential("")

# def res_schema(params):
