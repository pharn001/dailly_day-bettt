
from rest_framework import generics, status
from .serializers import BlogPostSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import status
# from .filters import BlogPostFilter
# class BlogPostListCreate(generics.ListCreateAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     filterset_class = BlogPostFilter # here
    
#     def delete(self, request, *args, **kwargs):
#         BlogPost.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer
#     lookup_field = "pk"    
class RegisterUserView(GenericAPIView):
    serializer_class = BlogPostSerializer

    def post(self, request):
        user_data=request.data
        serializer = self.serializer_class(data=user_data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user=serializer.data
             #send email function usr['email']
            return Response({
                'data':user,
                'message':f'hi {user.first_name} thanks for signing up '
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400)