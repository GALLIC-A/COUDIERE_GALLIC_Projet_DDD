from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test, Profession
from .serializers import ProfessionSerializer

@api_view(['GET'])
def get_tests(request):
    tests = Test.objects.all()
    # data = [t.texte for t in tests]
    # return Response(data)
    return Response({"tests": [test.texte for test in tests]})

@api_view(['GET'])
def search_profession(request):
    name = request.GET.get('name', '')
    professions = Profession.objects.find_by_name(name)
    serializer = ProfessionSerializer(professions, many=True)
    return Response(serializer.data)