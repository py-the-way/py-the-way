from parsel import Selector
import requests, sys

def indeed(data, params):

	for _, row in data.iterrows():

		try:

			url = f"https://www.indeed.com/jobs?q={params['title']}&l={row['geo_name']}"

			page = requests.get(url)
		
			selector = Selector(text=page.text)

			available = {}

			results = selector.css("#SALARY_rbo a::attr(title)").getall()

			# resultsSplit = [x.split(" ")]

			available[row['geo_name']] = results

			print(row["geo_name"], results)

		except:
			e = sys.exc_info()
			print(e)
			continue

	return available