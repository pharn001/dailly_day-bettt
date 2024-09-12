from django.urls import path
from .views import views

urlpatterns =[    
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path("blogposts/<int:pk>", views.BlogPostRetrieveUpdateDestory.as_view(), name="update"),
]