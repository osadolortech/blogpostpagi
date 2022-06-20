from rest_framework import viewsets
from .models import BlogpostList
from .serializers import Blogserielizers
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.

class BlogApi(viewsets.ModelViewSet):
    queryset = BlogpostList.objects.all()
    serializer_class = Blogserielizers
    

