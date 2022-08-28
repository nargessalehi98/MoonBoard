from core import fuzzification, defuzzification, inference


class Result(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Result, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(start, body) -> str:
        Fuzzification = fuzzification.Score()
        score = Fuzzification.get(start, body)

        Inference = inference.Inference()
        point = Inference.get(score)

        Defuzzification = defuzzification.Defuzzification()
        return Defuzzification.defuzzify(point)
