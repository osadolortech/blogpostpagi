from rest_framework import serializers
from .models import BlogpotslList


class Blogserilizers(serializers.ModelSerializer):
    class Meta:
        model = BlogpotslList
        fields =(
            'id', 'author','title','content','created_date'
        )