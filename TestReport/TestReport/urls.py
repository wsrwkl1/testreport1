#coding=utf-8 
from django.conf.urls import patterns, include, url
from TRR import views
from django.conf import settings
from django.contrib import admin
#from django.contrib.auth.views import login 
admin.autodiscover()

urlpatterns = patterns('',

)

urlpatterns += patterns('',
    
    #url(r'^login/$', views.login),
    #(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}), //如果你不想调用模板文件 registration/login.html ，那么可以在 URLconf 通过额外参数把 template_name 传递给视图。例如，以下的 URLconf 设置会使用 myapp/login.html 来代替缺省的模板:
    url(r'^accounts/login/$','django.contrib.auth.views.login',{
        'template_name':'registration/login.html',
    }),
)

urlpatterns += patterns('',
    (r'^medias/(?P<path>.*)','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
)

urlpatterns += patterns('',
    url(r'^$',views.home),
    url(r'^home/$',views.home),
    url(r'^index/$',views.index),
    url(r'^blinfo/$', views.blinfo),
    url(r'^currinfo/$',views.currinfo),
    url(r'^blsearch/$',views.blsearch),
    url(r'^currsearch/$',views.currsearch),
    #url(r'^blcompare/$',views.blcompare),
    url(r'^blComReasult/$',views.blComReasult),
    url(r'^currcompare/$',views.currcompare),
    url(r'^admin/', include(admin.site.urls)),
    
)
