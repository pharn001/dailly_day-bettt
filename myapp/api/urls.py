from django.urls import path
from .views import RegisterUserView
urlpatterns =[
    path("register/", RegisterUserView.as_view(), name="register"),

    # path("blogposts/<int:pk>", views.BlogPostRetrieveUpdateDestory.as_view(), name="update"),
]
