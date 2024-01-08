from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from . import models, forms


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Post
        fields = "__all__"
        lookup_field = "url"
        extra_kwargs = {"data": {"lookup_field": "url"}}
