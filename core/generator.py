import random
from map import Map


class Generator:
    def __init__(self):
        self.top = []
        self.start = []
        self.body = []
        self.length = 0
        self.map = Map()

    def _length_(self):
        self.length = random.randint(3, 11)

    def _start_(self):
        size = random.randint(1, 2)
        self.start = self.map.set_start(size)

    def _top_(self):
        self.top = self.map.set_top()

    def _start_limit_(self):
        start_limit = 0
        for hold in self.start:
            if int(hold[0]) > int(start_limit):
                start_limit = hold[0]
        return start_limit

    def alphabet_to_number(self, hold) -> (int):
        if hold.endswith('A'):
            return 0
        if hold.endswith('B'):
            return 1
        if hold.endswith('C'):
            return 2
        if hold.endswith('D'):
            return 3
        if hold.endswith('E'):
            return 4
        if hold.endswith('F'):
            return 5
        if hold.endswith('G'):
            return 6
        if hold.endswith('H'):
            return 7
        if hold.endswith('I'):
            return 8
        if hold.endswith('J'):
            return 9
        if hold.endswith('K'):
            return 10

    def get_row_of_hold(self, hold):
        if len(hold) == 3:
            return int(hold[0] + hold[1])
        if len(hold) == 2:
            return int(hold[0])

    def get_start_max(self):
        if len(self.start) == 2:
            return max(self.get_row_of_hold(self.start[0]), self.get_row_of_hold(self.start[1]))
        return self.get_row_of_hold(self.start[0])

    # TODO read path
    def get_next_hold(self):
        pre_hold = '1A'
        while self.get_row_of_hold(pre_hold) < 17:
            if len(self.body) == 0:
                # print("start_limit: " + str(self.get_start_max()))
                self.body.append(
                    f'{str(random.randint(self.get_start_max(), self.get_start_max() + 6))}{random.choice(self.map.letters)}')
            else:
                pre_hold = self.body[len(self.body) - 1]
                # print("pre_hold: " + pre_hold)
                if self.get_row_of_hold(pre_hold) + 6 >= 18:
                    end = 17
                else:
                    end = self.get_row_of_hold(pre_hold) + 6
                self.body.append(
                    f'{random.randint(self.get_row_of_hold(pre_hold), end)}{random.choice(self.map.letters)}')

    def _body_(self):
        self._length_()
        self._start_()
        self._top_()
        # start = self._start_limit_()
        self.get_next_hold()
        # for i in range(1, int(self.length)):
        #     self.body.append(f'{random.randint(int(start), 17)}{random.choice(self.map.letters)}')

    def get_body(self):
        self._body_()
        return self.body

    def draw_board(self):
        start_color = '\033[92m'
        finish_color = '\033[91m'
        move_color = '\033[94m'
        end_color = '\033[0m'
        result = 'A B C D E F G H I J K'
        body = self.get_body()
        print(self.start + self.body + self.top)
        print(result)
        for row in range(18, 0, -1):
            one_row = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
            for hold in self.start:
                if row == int(self.get_row_of_hold(hold)):
                    one_row[self.alphabet_to_number(hold)] = start_color + "H" + end_color
            for hold in self.top:
                if row == int(self.get_row_of_hold(hold)):
                    one_row[self.alphabet_to_number(hold)] = finish_color + "H" + end_color
            for hold in body:
                if row == int(self.get_row_of_hold(hold)):
                    one_row[self.alphabet_to_number(hold)] = move_color + "H" + end_color

            print(*one_row, end="")
            print(" " + str(row))


g = Generator()
g.draw_board()
