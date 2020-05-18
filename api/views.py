from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import IdeaSerializer

from ideas.models import Idea

class IdeaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ideas to be viewed or edited.
    """
    queryset = Idea.objects.all().order_by('-pub_date')
    serializer_class = IdeaSerializer

class IdeaApiView(APIView):

    def get(self, request, pk=None):
        res = get_object_or_404(Idea, pk=pk)
        
        return Response ({"msg": res, status:status.HTTP_200_OK})
