from rest_framework import serializers

from post.models import Post, Comments
from post.validators import LegalWordsValidator

TABOO = [
    'ерунда', 'глупость', 'чепуха', 'eрунда', 'epунда',
    'epyнда', 'epyндa', 'глyпость', 'глyпoсть', 'глyпоcть',
    'глyпосtь', 'чeпуха', 'чeпyха', 'чeпуxа', 'чeпухa'
]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    title = serializers.CharField(max_length=50, validators=[LegalWordsValidator(TABOO)])


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
