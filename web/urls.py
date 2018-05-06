from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = (
    url(r'^$', TemplateView.as_view(template_name='web/index.html')),
    url(r'^login/$', TemplateView.as_view(template_name='web/login.html')),
    url(r'^reserve/0/$', TemplateView.as_view(template_name='web/reserve_0.html')),
    url(r'^reserve/1/$', TemplateView.as_view(template_name='web/reserve_1.html')),
    url(r'^reserve/2/$', TemplateView.as_view(template_name='web/reserve_2.html')),
    url(r'^reserve/3/$', TemplateView.as_view(template_name='web/reserve_3.html')),
    url(r'^reserve/4/$', TemplateView.as_view(template_name='web/reserve_4.html')),
    url(r'^reserve/5/$', TemplateView.as_view(template_name='web/reserve_5.html')),
    url(r'^signup/1/$', TemplateView.as_view(template_name='web/signup_1.html')),
    url(r'^signup/2/$', TemplateView.as_view(template_name='web/signup_2.html')),
    url(r'^signup/3/$', TemplateView.as_view(template_name='web/signup_3.html')),
    url(r'^signup/4/$', TemplateView.as_view(template_name='web/signup_4.html')),
)
