from django.shortcuts import render

# Create your views here.
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

"""
In Django REST Framework (DRF), APIView is a class-based view used to define custom behaviors for your API endpoints. The SnippetDetail class you provided is a custom view that allows you to retrieve, update, or delete a specific Snippet instance. Here's a detailed explanation of each part of the class:

Docstring
python
Copy code

This is a docstring that describes the purpose of the class. It explains that the class is
 used to retrieve, update, or delete a snippet instance.
get_object Method
python
Copy code
def get_object(self, pk):
    try:
        return Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        raise Http404
Purpose: This method retrieves a Snippet instance by its primary key (pk).
How it works: It tries to get the Snippet instance from the database using Snippet.objects.get(pk=pk).
 If the snippet does not exist, it raises an Http404 exception, which returns a 404 Not Found 
 response to the client.
get Method
python
Copy code
def get(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = SnippetSerializer(snippet)
    return Response(serializer.data)
Purpose: This method handles GET requests to retrieve a Snippet instance.
How it works: It calls the get_object method to get the Snippet instance. Then, it serializes 
the snippet using SnippetSerializer and returns the serialized data in the response.
put Method
python
Copy code
def put(self, request, pk, format=None):
    snippet = self.get_object(pk)
    serializer = SnippetSerializer(snippet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
Purpose: This method handles PUT requests to update a Snippet instance.
How it works: It calls the get_object method to get the Snippet instance. Then,
 it creates a SnippetSerializer with the snippet instance and the new data from 
 the request (request.data). If the serializer is valid, it saves the updated 
 snippet and returns the serialized data. If the serializer is not valid, it
   returns the errors with a 400 Bad Request status.
delete Method
python
Copy code
def delete(self, request, pk, format=None):
    snippet = self.get_object(pk)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
Purpose: This method handles DELETE requests to delete a Snippet instance.
How it works: It calls the get_object method to get the Snippet instance. Then, 
it deletes the snippet and returns a response with a 204 No Content status, 
indicating that the deletion was successful.
Summary
get_object(self, pk): Retrieves a snippet by primary key or raises a 404 error if not found.
get(self, request, pk, format=None): Retrieves and returns a snippet.
put(self, request, pk, format=None): Updates a snippet with the provided data if valid, 
otherwise returns validation errors.
delete(self, request, pk, format=None): Deletes a snippet and returns a 204 No Content 
response.
This class leverages Django REST Framework's APIView to define a detail view for snippets,
 providing full CRUD (Create, Read, Update, Delete) functionality for individual Snippet instances.

"""