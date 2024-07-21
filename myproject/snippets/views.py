from django.shortcuts import render


from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

"""
CreateModelMixin: Provides create behavior for handling POST requests.
ListModelMixin: Provides list behavior for handling GET requests that list multiple objects.
"""
    
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





"""
Explanation
Importing Mixins: You import the mixins you need from rest_framework. 
In this case, RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin.

Combining Mixins with GenericAPIView: Instead of subclassing APIView, you 
subclass GenericAPIView and mix in the specific behavior you need. Here, 
RetrieveModelMixin, UpdateModelMixin, and DestroyModelMixin are mixed in.

Setting Queryset and Serializer: You set the queryset and serializer_class
 attributes to tell the view which model and serializer to use.

Defining HTTP Methods: You define the HTTP methods (get, put, delete) to use 
the mixin methods (retrieve, update, destroy). These mixin methods handle the
 common behavior for these operations.

"""
"""
Summary
Using mixins in Django REST Framework helps you to compose views by combining small, reusable classes
 that encapsulate common behavior. This approach reduces code duplication and makes your views more
   manageable and easier to understand. By using mixins, you can easily create views that handle 
   common CRUD operations in a consistent manner.

"""