# from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TemplateSerializer
from .models import DefaultTemplate
# Create your views here.

class DefaultTemplatesDetails(APIView):
    # List all templates or create new template
    def get(self, request, format=None):
        # Get all templates
        templates = DefaultTemplate.objects.all()
        serializer = TemplateSerializer(templates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Create a template
        serializer = TemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DefaultTemplatesManipulation(APIView):
    """
    These route should be restricted in the future
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, slug):
        try:
            return DefaultTemplate.objects.get(slug=slug)
        except DefaultTemplate.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        template = self.get_object(slug)
        serializer = TemplateSerializer(template)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        template = self.get_object(slug)
        serializer = TemplateSerializer(template, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        template = self.get_object(slug)
        template.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)