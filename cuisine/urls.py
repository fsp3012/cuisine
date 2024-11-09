# from django.conf.urls import url
from django.urls import re_path as url
from django.urls import path
from . import views

urlpatterns = [

    #Cuisine_list view as a class-based view
    url(r'^$',
        views.CuisineListView.as_view(),
        name='Cuisine_list'
        ),
        
    # Cuisine_list view as a function
    # url(r'^$',
    #     views.Cuisine_list,
    #     name='Cuisine_list'
    #     ),


    #Cuisine_detail view as a class-based view
    # path('<slug:slug>', 
    #         views.CuisineDetailView.as_view(), 
    #         name='Cuisine_detail',
    # ),

    # Cuisine_detail view as a function
    url(
        r'^(?P<cuisine>[-\w]+)/$',
        views.Cuisine_detail,
        name='Cuisine_detail'
    ),


]
