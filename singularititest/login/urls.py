from django.views.generic.base import TemplateView
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from login import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='login/home.html'), name='home'),
    url(r'^logout/$', TemplateView.as_view(template_name='login/logged_out.html'), name='logout'),
    url(r'^login/$', views.snippet_login, name='login'),
    url(r'^signup/$', views.snippet_signup, name='signup'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
