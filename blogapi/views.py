from rest_framework import viewsets
from .models import BlogpotslList
from .serializers import Blogserilizers
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.

class BlogApi(viewsets.ModelViewSet):
    queryset = BlogpotslList.objects.all()
    serializer_class = Blogserilizers
    pagination_class = LimitOffsetPagination

