#Import django function path and all of our views
#from the blog app.
from django.urls import path
from . import views

urlpatterns = [
    #assign post_list view to root url
    path('',views.post_list,name='post_list'),
    path('tester/',views.test,name='test'),
]