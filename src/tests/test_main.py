from start import View_Residential
# test url: http://127.0.0.1:5002/res/order/2/5/4/1/3/prefs/100000/200000/0.3/tech/jobs/computer+science/100000
import unittest, json


class TestMain(unittest.TestCase):

	def test_get(self):

		res_test = View_Residential()
		res_test.get(
			
			1, 2, 3, 4, 5,
			100000, 200000, 0.3, "tech",
			"computer+science", 100000

		)

		self.assertTrue("geo_name" in res_test.test_data.r.output.keys())


unittest.main()