from django.conf.urls import include,url

from . import views
from django.contrib.auth import views as auth_views
app_name = 'polls'
urlpatterns = [
    url(r'^account/login/$',views.alogin),
    url(r'^account/register/$',views.register,name='register'),
    url(r'^account/logout/$',views.alogout,name='logout'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]