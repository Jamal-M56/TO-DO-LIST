from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from task.models import *
# Create your views here.

@api_view(['GET'])
def task(request):

    queryset = Task.objects.all()

    serializer = TaskSerializer(queryset,many=True)

    return Response(
        {'task':serializers.data},status=200
        )

