from recommender import Residential, Recommender

test_data = Residential(1,2,3,4,6,5)

test_data.set_prefs(10000,200000,True,"tech")

r = Recommender("residential",test_data)
