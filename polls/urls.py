from django.conf.urls import include,url

from . import views
from django.contrib.auth import views as auth_views
app_name = 'polls'


account_pattern = [

    url(r'^login/$',views.alogin),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.alogout,name='logout'),

]

urlpatterns = [

    
    url(r'^account/',include(account_pattern)),
    #url(r'^account/register/$',views.register,name='register'),
    #url(r'^account/logout/$',views.alogout,name='logout'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^cms/index/$', views.cmsIndex, name='cmsIndex'),
    url(r'^cms/web/(?P<filename>\w+)/$', views.cmsWeb, name='cmsWeb'),


    url(r'^(?:question-(?P<question_id>[0-9]+))/', include([
            url(r'^detail/$', views.detail, name='detail'),
            url(r'^results/$', views.results, name='results'),
            url(r'^vote/$', views.vote, name='vote'),
            url(r'^ans/$', views.answerQuestion, name='ansQuestion'),
        ])),
    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<doc_id>[0-9]+)/read/$', views.readDoc, name='readdoc'),
    url(r'^upload/$', views.upload_file, name='adddoc'),
    # url(r'^(?P<question_id>[0-9]+)/ans/$', views.answerQuestion, name='ansQuestion'),

]