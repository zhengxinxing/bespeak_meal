from django.conf.urls import patterns, url

from bespeak_meal import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'), # name 用于 template，实现非耦合的 URL
    url(r'^order/$', views.order, name='order'),
    #url(r'', views.xx, name=''),
    #url(r'', views.xx, name=''),
    #url(r'', views.xx, name=''),
    #url(r'', views.xx, name=''),
)