from parsel import Selector
import requests, sys
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()

def indeed(data, params):

	available = {}

	for _, row in data.iterrows():

		try:
			url = f"https://www.indeed.com/jobs?q={params['title']}&l={row['geo_name']}"

			page = requests.get(url)
		
			selector = Selector(text=page.text)

			results = selector.css("#SALARY_rbo a::attr(title)").getall()
			resultsSplit = [[int(x.split(" ")[0][1:].replace(",","")), int(x.split(" ")[1][1:-1])] for x in results]
			available[row['geo_name']] = resultsSplit

			print(row["geo_name"], resultsSplit)

		except:
			e = sys.exc_info()
			print(e)
			continue

	return available

def cal_top(jobs, data, params):

	# find closest pay grade per location
	closest_pay = {}
	closest_available = {}

	for cl in jobs.keys():
		latest = [jobs[cl][0][0], abs(params.jobs['pay'] - jobs[cl][0][0]), 0]

		for i, val in enumerate(jobs[cl][1:]):
			new_val = abs(params.jobs['pay'] - val[0])
			if new_val < latest[1]:
				latest = [val[0], new_val, i+1]

		closest_pay[cl] = jobs[cl][latest[2]][0]
		closest_available[cl] = jobs[cl][latest[2]][1]

	# map jobs to Dataframe
	data['jobs_pay'] = data['geo_name'].map(closest_pay)
	data['jobs_available'] = data['geo_name'].map(closest_available)

	# sort by available jobs and prefs

	# - scale available jobs and prefs
	scaled_jobs = min_max_scaler.fit_transform(data[['jobs_available']])
	scaled_prefs = min_max_scaler.fit_transform(data[['prefs']])

	# - then scale the sum of both of them for easy reading
	data['jobs+prefs'] =  min_max_scaler.fit_transform(scaled_jobs + scaled_prefs)

	data = data.sort_values("jobs+prefs", ascending=False)

	return data