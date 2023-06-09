from django.urls import path

from post.views import PostCreateView, CommentCreateView, PostListView, PostRetrieveView, PostUpdateView, \
    PostDestroyView, CommentListView, CommentRetrieveView, CommentUpdateView, CommentDestroyView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostRetrieveView.as_view(), name='post_id'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDestroyView.as_view(), name='post_del'),


    path('comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/', CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>/', CommentRetrieveView.as_view(), name='comment_id'),
    path('comment/update/<int:pk>/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/delete/<int:pk>/', CommentDestroyView.as_view(), name='comment_del'),
]

