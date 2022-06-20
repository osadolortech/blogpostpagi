from rest_framework import serializers
from .models import BlogpostList


class Blogserielizers(serializers.ModelSerializer):
    class Meta:
        model = BlogpostList
        fields =(
            'id', 'author','title','content','created_date'
        )