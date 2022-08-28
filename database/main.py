from score_calculator import Calculator


def get_database_path_grade_range():
    start = list(input().split(" "))
    body = list(input().split(" "))
    while len(start) != 0:
        c = Calculator(start, body)
        print(c.grader())
        print("Enter new path data:")
        start = list(input().split(" "))
        body = list(input().split(" "))


if __name__ == '__main__':
    get_database_path_grade_range()
