from django.conf.urls import url
'''import everything from views. here . import means we are
importing from the same folder the urls.py is located, here it is blog directory'''
from . import views

'''add urls patterns'''
urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
]
