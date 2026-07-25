from django.urls import path
from blog.views import home_view, comment_create


urlpatterns = [
    path('', home_view, name="home"),
    path('comment/create/', comment_create, name="comment-create"),
]
