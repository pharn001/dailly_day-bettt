from django.urls import path
from . import views
urlpattern =[
    path("blogposts/", views.BlogPostListCreate.as_views(), name="blogpost-view-create")
]
