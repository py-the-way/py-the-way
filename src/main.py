from recommender import Residential, Recommender

test_data = Residential(2,6,5,4,1,3)

test_data.set_prefs(100000,200000,True,"tech")

r = Recommender("residential",test_data)

print(r.output)
