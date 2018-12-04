from rest_framework.serializers import ModelSerializer
from blog.models import Blog

class BlogSerializer(ModelSerializer):
	class Meta:
		model=Blog
		fields=('id','title','content','published')

class BlogCreateSerializer(ModelSerializer):
	class Meta:
		model=Blog
		fields=('title','content','published')

class BlogUpdateSerializer(ModelSerializer):
	class Meta:
		model=Blog
		fields=('id','title','content')
