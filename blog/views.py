from rest_framework.generics import(
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
)
from blog.models import Blog
from blog.serializers import (
	BlogSerializer,
	BlogCreateSerializer,
	BlogUpdateSerializer
)

class PostCreateView(CreateAPIView):
	queryset=Blog.objects.all()
	serializer_class= BlogCreateSerializer

class PostDeleteView(DestroyAPIView):
	queryset=Blog.objects.all()
	serializer_class=BlogSerializer
	lookup_field='pk'

class PostListView(ListAPIView):
	queryset=Blog.objects.all()
	serializer_class=BlogSerializer


class PostRetrieveView(RetrieveAPIView):
	queryset=Blog.objects.all()
	serializer_class=BlogSerializer
	lookup_field = 'pk'


class PostUpdateView(RetrieveUpdateAPIView):
	queryset=Blog.objects.all()
	serializer_class=BlogUpdateSerializer
	lookup_field='pk'