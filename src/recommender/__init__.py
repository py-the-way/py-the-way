from recommender.weighter import residential
from recommender.engine import res_choose
import inspect, json

class Recommender:
    def __init__(self, mode, params):
        if mode == "residential":
            self.residential(params)

    def residential(self, params):

        r = residential(params)

        # get top 10 choices
        top = res_choose(r, params, 15)

        print(top)

        # convert to JSON for REST
        self.output = top.to_dict(orient='records')

class Residential:
    # will be equal to an order index
    def __init__(self, education, jobs, home, health, wealth):

        frame = inspect.currentframe()
        args,_,_,vals = inspect.getargvalues(frame)

        for v in args[1:]:
            self.__dict__[vals[v]] = v

    def set_prefs(self, pop, price, urban, industry):

        # pop will be a number from 1000 ->1000000

        frame = inspect.currentframe()
        args,_,_,vals = inspect.getargvalues(frame)

        self.prefs = {}

        for v in args[1:]:
            self.prefs[v] = vals[v]


    def __getitem__(self,key):
        return self.__dict__[key]
    
    def is_int(self, i):
        try:
            int(i)
            return True
        except:
            return False

    def keys(self):
        return [k for k in self.__dict__.keys() if self.is_int(k)]

    def order(self):
        return sorted([k for k in self.__dict__ if self.is_int(k)])

    def __str__(self):
        return repr(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)
