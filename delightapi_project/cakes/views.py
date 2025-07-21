from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cake
from .serializers import CakeSerializer
from django.shortcuts import render

@api_view(['GET'])
def get_all_cakes(request):
    cakes = Cake.objects.all()
    serializer = CakeSerializer(cakes, many=True)
    return Response(serializer.data)

def cake_list_view(request):
    cakes = Cake.objects.all()
    return render(request, 'cake_list.html', {'cakes': cakes})

