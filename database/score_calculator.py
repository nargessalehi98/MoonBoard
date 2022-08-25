import math

from core.map import Map


class Calculator:
    def __init__(self, start, path):
        self.map = Map()
        self.path = path
        self.start = start

    def cal_distance(self, hold1, hold2):
        ver_dis = math.fabs(self.map.get_row_of_hold(hold1) - self.map.get_row_of_hold(hold2))
        hor_dis = math.fabs(self.map.alphabet_to_number(hold1) - self.map.alphabet_to_number(hold2))
        return math.sqrt(math.pow(ver_dis, 2) + math.pow(hor_dis, 2))

    def grader(self):
        score = 0
        start_len = len(self.start)
        start = self.start

        if start_len == 1:
            score += 2 * (self.map.get_score(self.start[0]))
            # score += math.pow(self.map.get_score(self.start[0]), 2)
        elif start_len == 2:
            score += (self.map.get_score(self.start[0])) + (self.map.get_score(self.start[1]))

        # for hold in self.start:
        #     score += self.map.get_score(hold)

        for i in range(0, len(self.path)):
            if start_len == 2 and i == 0:
                if self.cal_distance(start[0], self.path[i]) > self.cal_distance(start[1], self.path[i]):
                    score += (self.map.get_score(self.path[i])) * (self.cal_distance(start[1], self.path[i]))
                    start.pop(1)
                else:
                    score += (self.map.get_score(self.path[i])) * (self.cal_distance(start[0], self.path[i]))
                    start.pop(0)
            elif start_len == 2 and i == 1:
                score += (self.map.get_score(self.path[i])) * (self.cal_distance(start[0], self.path[i]))
            elif start_len == 1 and i == 0:
                score += (self.map.get_score(self.path[i])) * (self.cal_distance(start[0], self.path[i]))
            elif start_len == 1 and i == 1:
                score += (self.map.get_score(self.path[i])) * (self.cal_distance(start[0], self.path[i]))
            elif i >= 2:
                if self.cal_distance(self.path[i - 1], self.path[i]) > self.cal_distance(self.path[i - 2],
                                                                                         self.path[i]):
                    score += (self.map.get_score(self.path[i])) * (self.cal_distance(self.path[i - 2], self.path[i]))
                else:
                    score += (self.map.get_score(self.path[i])) * (self.cal_distance(self.path[i - 1], self.path[i]))
        return score / (len(self.path))
