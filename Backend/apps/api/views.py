from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test

@api_view(['GET'])
def get_tests(request):
    tests = Test.objects.all()
    # data = [t.texte for t in tests]
    # return Response(data)
    return Response({"tests": [test.texte for test in tests]})
