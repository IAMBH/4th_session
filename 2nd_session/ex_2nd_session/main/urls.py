from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('intro/', interestpage, name='interestpage'),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('post/', post, name='post'),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('tag/', tag_list, name="tag_list"),
    path('tag/<int:tag_id>', tag_posts, name="tag_posts"),
    path('delete_com/<int:id>', delete_com, name="delete_com"),
    # img urls
    # path('edit_img/<int:id>', edit_img, name="edit_img"),
    # path('update_img/<int:id>', update_img, name="update_img"),
    # path('delete_img/<int:id>', delete_img, name="delete_img"),
]