from django.urls import path


from . import views 

app_name = "posts" # designated that the url_patterns belong to the posts app


urlpatterns = [
    path('',views.posts_list, name="list"),# the name is used to refer to this path in other templates
    path('<slug:slug>',views.post_page, name="page"),
]
