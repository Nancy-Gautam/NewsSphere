from django.urls import  path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('jobs/',views.myjobs),
    path('videos/',views.videos),
    path('news/',views.news),
    path('viewnews/',views.viewnews),
    path('mprofile/',views.mprofile),

]