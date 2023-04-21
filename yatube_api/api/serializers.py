from posts.models import Comment, Group, Post

from rest_framework.serializers import ModelSerializer, SlugRelatedField


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('post',)


class GroupSerializer(ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
