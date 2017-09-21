from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^delete/(?P<id>\d+)$', views.delete),
url(r'^delete_course$', views.delete_course),
url(r'^comments/(?P<id>\d+)$', views.comments),
url(r'^comments/add_comment$', views.add_comment),
url(r'^add_course$', views.add_course)
]