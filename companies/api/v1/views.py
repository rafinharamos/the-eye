from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from companies.api.v1.serializers import CompanySerializer


class CompanyView(APIView):
    """
    post:
    Create a new company instance.
    """

    serializer_class = CompanySerializer

    def post(self, request):
        serializer = CompanySerializer(data=request.data or None)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
