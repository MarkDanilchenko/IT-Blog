from rest_framework import serializers
from rest_framework.settings import api_settings
from taggit.models import Tag
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from . import models, forms


class UserSerializer(serializers.ModelSerializer):
    # SIGN UP method
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email = validated_data["email"]
        phone = validated_data["phone"]
        if phone == "":
            phone = None
        user = models.User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
        )
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = models.User
        fields = "__all__"


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tag = TagListSerializerField()
    author = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = models.Post
        fields = "__all__"
        lookup_field = "url"
        extra_kwargs = {"data": {"lookup_field": "url"}}


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("slug",)
        lookup_field = "slug"
        extra_kwargs = {"data": {"lookup_field": "slug"}}


class FeedbackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(max_length=100, required=True)
    theme = serializers.CharField(max_length=150, min_length=1, required=True)
    message = serializers.CharField(max_length=1000, min_length=1, required=True)


class Post_CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    # The line `created_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)` in the
    # `Post_CommentSerializer` class is defining a serializer field for the `created_at` attribute of
    # the `Post_Comment` model. Read-only mode is used to convert the datetime object to a definite string format in the RESPONSE ONLY.
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = models.Post_Comment
        fields = "__all__"
