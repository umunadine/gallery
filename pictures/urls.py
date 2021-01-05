from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.gallery,name='gallery'),
    url(r'^search/', views.search_by_cat, name='search_by_cat'),
    
]