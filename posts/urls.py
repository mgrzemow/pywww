from django.urls import path
from .views import posts_list, posts_details, posts_add

app_name='posts'

urlpatterns = [
    path('', posts_list, name='list'),
    path('<int:post_id>', posts_details, name='details'),
    path('add', posts_add, name='add'),
]
