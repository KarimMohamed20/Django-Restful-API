from django.conf.urls import url
from blog.views import (
	PostCreateView,
	PostDeleteView,
	PostListView,
	PostRetrieveView,
	PostUpdateView
)

app_name='blog'

urlpatterns = [

	url(r'^api/blog/create/$',PostCreateView.as_view(),name='List'),
	url(r'^api/blog/delete/(?P<pk>[\d-]+)/$',PostDeleteView.as_view(),name='Delete'),
	url(r'^api/blog/$',PostListView.as_view(),name='List'),
	url(r'^api/blog/(?P<pk>[\d-]+)/$',PostRetrieveView.as_view(),name='Retrieve'),
	url(r'^api/blog/update/(?P<pk>[\d-]+)/$',PostUpdateView.as_view(),name='Update'),


]

