from django.urls import path
from . import views


urlpatterns=[
  path('',views.home_page,name='home_page'),
  path('join/union/<union_id>',views.join_union,name='join_union'),
  path('union/emergency-services',views.e_services,name='e_services'),
  path('union/businesses',views.union_bs,name='union_bs'),
  path('union/posts',views.union_posts,name='union_posts'),
  path('union/myprofile',views.my_profile,name='my_profile'),
  path('union/search/business',views.search_business,name='search_business')
]