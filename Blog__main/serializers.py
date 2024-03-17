from rest_framework import serializers
from taggit.models import Tag
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from . import models


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        username = validated_data["username"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        email = validated_data["email"]
        phone = validated_data["phone"]
        password = validated_data["password"]
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
    created_at = serializers.DateField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = models.Post
        fields = "__all__"
        lookup_field = "url"
        extra_kwargs = {"data": {"lookup_field": "url"}}
        # In the `PostSerializer` class, `lookup_field = "url"` and `extra_kwargs = {"data":
        # {"lookup_field": "url"}}` are used to specify the field to be used as the lookup field instead of the default "pk" when
        # retrieving or updating instances of the `Post` model.


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("slug",)
        lookup_field = "slug"
        extra_kwargs = {"data": {"lookup_field": "slug"}}
        # In the `TagSerializer` class, `lookup_field = "slug"` and
        # `extra_kwargs = {"data": {"lookup_field": "slug"}}` are used to specify the field to be used
        # as the lookup field instead of the default "pk" when retrieving or updating instances of the `Tag` model.


class FeedbackSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    theme = serializers.CharField(max_length=150, min_length=1, required=True)
    message = serializers.CharField(max_length=1000, min_length=1, required=True)


class Post_CommentsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = models.Post_Comments
        fields = "__all__"
