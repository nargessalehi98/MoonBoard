from core.generator import Generator
from core.result import Result
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class Route(APIView):

    def get(self, request):
        generator = Generator()
        start = generator.get_start()
        body = generator.get_body()
        top = generator.get_top()
        generator.draw_board()
        result = Result()
        output = {
            "grade": result.get_final_result(start, body + top),
            "start": start,
            "body": body,
            "top": top
        }
        return Response(data=output, status=HTTP_200_OK)


if __name__ == '__main__':
    generator = Generator()
    result = Result()
    start = generator.get_start()
    body = generator.get_body()
    generator.draw_board()
    top = generator.get_top()
    generator.draw_board()
    print(result.get_final_result(start, body + top))
