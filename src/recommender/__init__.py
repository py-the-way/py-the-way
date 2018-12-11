from recommender.weighter import residential
import inspect

class Recommender:
    def __init__(self, mode, params):
        if mode == "residential":
            self.residential(params)

    def residential(self, params):
        residential(params)

class Residential:
    # will be equal to an order index
    def __init__(self, education, jobs, hapiness, weather):

        frame = inspect.currentframe()
        args,_,_,vals = inspect.getargvalues(frame)

        for v in args[1:]:
            self.__dict__[vals[v]] = v

    def __getitem__(self,key):
        return self.__dict__[key]

    def __str__(self):
        return repr(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)
