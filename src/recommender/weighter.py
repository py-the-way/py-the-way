import pandas as pd
from sklearn import preprocessing
import os

def normalise(data, to, fro, imp):
	data[to] = ((data[fro] 
		- data[fro].mean()) 
		/ (data[fro].max() 
		- data[fro].min()))*imp

# https://api.datausa.io/api/join/csv?show=geo&sumlevel=county&required=adult_obesity,pop,income_below_poverty,high_school_graduation,unemployment,violent_crime,age,median_property_value,grads_total,population_living_in_a_rural_area,owner_occupied_housing_units&sort=desc&order=pop&display_names=1&limit=80000&year=latest
# https://api.datausa.io/api/join?=
min_max_scaler = preprocessing.MinMaxScaler()

def residential(params):

	print(params)

	# geo_name,geo_id,pop,adult_obesity,income_below_poverty,high_school_graduation,unemployment,violent_crime,age,median_property_value,owner_occupied_housing_units,population_living_in_a_rural_area,grads_total

	data_cols = ["geo_name","geo_id","pop","obesity","poverty",
	"high_school_graduation","unemployment","violent_crime",
	"age","median_property_value",
	"own_housing_percentage",
	"rural","grads_total"]

	path = str(os.path.dirname(os.path.realpath(__file__)))

	data = pd.read_csv(path+"/../../data/data1.csv", sep=",", names=data_cols, encoding="latin-1")

	# weight data and return

	imp = 1
	# weighter. this decreases importance by .1 for each param
	for i in params.order():

		# make sure best option is highest

		if params[i] == "education":

			normalise(data, "grads_total", "grads_total", 1)
			normalise(data, "high_school_graduation", "high_school_graduation", 1)
			
			data["education"] = data["high_school_graduation"] + data["grads_total"]
			
			normalise(data, "education", "education", 1)

			order = data[["education"]]
			o_scaled = min_max_scaler.fit_transform(order)
			order = pd.DataFrame(o_scaled)
			data[["education"]] = order*imp
 
		elif params[i] == "jobs":

			# as we want lowest unemployment
			normalise(data, "employment", "unemployment", -1)

			order = data[["employment"]]
			o_scaled = min_max_scaler.fit_transform(order)
			order = pd.DataFrame(o_scaled)
			data[["employment"]] = order*imp

		elif params[i] == "health":

			# as violent crimes is per 100,000
			data["health"] = data["obesity"] + (data["violent_crime"] / 100000)

			normalise(data, "health", "health", -1)

			order = data[["health"]]
			o_scaled = min_max_scaler.fit_transform(order)
			order = pd.DataFrame(o_scaled)
			data[["health"]] = order*imp

		elif params[i] == "home":

			normalise(data, "home", "own_housing_percentage", 1)

			order = data[["home"]]
			o_scaled = min_max_scaler.fit_transform(order)
			order = pd.DataFrame(o_scaled)
			data[["home"]] = order*imp

		elif params[i] == "wealth":

			normalise(data, "wealth", "median_property_value", 1)

			order = data[["wealth"]]
			o_scaled = min_max_scaler.fit_transform(order)
			order = pd.DataFrame(o_scaled)
			data[["wealth"]] = order*imp


		imp -= .2

	data["population"] = data["pop"]

	for k in params.prefs.keys():

		# the best is closest to 0 for these

		if k == "pop":

			data["pop"] = abs(params.prefs[k] - data["pop"])
			
		elif k == "price":

			data["price"] = abs(params.prefs[k] - data["median_property_value"])

		elif k == "urban":

			# urban should be a percentage

			data["urban"] = abs(params.prefs[k] - (1 - data["rural"]))


	# now normalise the data once again using sklearn


	prefs = data[["pop", "price", "urban"]]
	p_scaled = min_max_scaler.fit_transform(prefs)
	prefs = pd.DataFrame(p_scaled)
	data[["pop", "price", "urban"]] = prefs


	return {
		"order": data[["geo_name", "geo_id", "education", "employment", "health", "home", "wealth"]],
		"prefs": data[["geo_name", "geo_id", "pop", "price", "urban",    "population", "median_property_value"]]
	}

