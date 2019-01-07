from recommender import Residential, Recommender

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonpify

app = Flask(__name__)
api = Api(app)

class View_Residential(Resource):
    
    def get(
        self,
        education, jobs, home, health, wealth,
        pop, price, urban, industry,
        title, pay
    ):
        test_data = Residential(int(education), int(jobs), int(home), 
        int(health), int(wealth))
        # test_data = Residential(2,5,4,1,3)

        test_data.set_prefs(int(pop), int(price), float(urban), str(industry))

        test_data.set_jobs(title, int(pay))

        # test_data.set_prefs(100000,200000,True,"tech")

        r = Recommender("residential", test_data)

        return jsonpify(r.output)

api.add_resource(View_Residential, '/res/order/<education>/<jobs>/<home>/<health>/<wealth>/prefs/<pop>/<price>/<urban>/<industry>/jobs/<title>/<pay>')

# test url: http://127.0.0.1:5002/res/order/2/5/4/1/3/prefs/100000/200000/0.3/tech/jobs/computer+science/100000

app.run(port='5002')