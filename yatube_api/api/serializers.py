import base64
from django.core.files.base import ContentFile

from rest_framework.serializers import (ModelSerializer,
                                        CurrentUserDefault,
                                        ValidationError,
                                        ImageField,
                                        )
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import User, Follow, Group, Comment, Post


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=CurrentUserDefault())
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]

    def validate(self, data):
        if data['following'] == self.context['request'].user:
            raise ValidationError(
                "Вы не можете подписаться сами на себя"
            )
        return data


class GroupsSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class Base64ImageField(ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64')
            ext = format.split('/')[1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)
