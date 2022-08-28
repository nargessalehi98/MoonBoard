from core.generator import Generator
from core.result import Result
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class Route(APIView):

    @staticmethod
    def get(request):
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
