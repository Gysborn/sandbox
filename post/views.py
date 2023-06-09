from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError

from post.permissions import IsOwnerOrAdmin
from post.models import Post, Comments
from post.serializers import PostSerializer, CommentSerializer, PostCreateSerializer


# Create your views here.
class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs): # Здесь мы проверяем достиг ли автор поста 18 ти
        from datetime import date
        birthday = request.user.birthday
        today = date.today()
        age = today.year - birthday.year - (today.timetuple()[1:3] < birthday.timetuple()[1:3])
        if age < 18:
            raise ValidationError("Публиковать посты можно с 18 лет")
        else:
            request.data['author'] = request.user.id
            return super().create(request, *args, **kwargs)


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]


class PostRetrieveView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]


class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAdmin, ]


class PostDestroyView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrAdmin, ]


class CommentCreateView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        return super().create(request, *args, **kwargs)


class CommentListView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]


class CommentRetrieveView(RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]


class CommentUpdateView(UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrAdmin, ]


class CommentDestroyView(DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrAdmin, ]
