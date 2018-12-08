import recommender.weighter as w

class Recommender:
    def __init__(self, mode, params):
        if mode == "residential":
            self.residential(params)

    def residential(self, params):
        w.residential(params)
