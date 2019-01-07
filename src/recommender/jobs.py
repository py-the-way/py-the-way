from parsel import Selector
import requests, sys

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

def cal_top(jobs, data, pay):

	# find closest pay grade per location
	closest_pay = {}
	closest_available = {}

	for cl in jobs.keys():
		latest = 0
		for i, val in enumerate(jobs[cl]):
			new_val = abs(pay - val[0])
			if new_val < latest:
				latest = i
		closest_pay[cl] = jobs[cl][latest][0]
		closest_available[cl] = jobs[cl][latest][1]

	# map jobs to Dataframe
	data['jobs_pay'] = data['geo_name'].map(closest_pay)
	data['jobs_available'] = data['geo_name'].map(closest_available)

	# sort by available jobs
	data.sort_values("jobs_available", ascending=False)

	return data