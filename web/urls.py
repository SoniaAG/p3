from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = (
    url(r'^$', TemplateView.as_view(template_name='web/index.html'), name='index'),
    url(r'^login/$', TemplateView.as_view(template_name='web/login.html'), name='login'),
    url(r'^reserve/0/$', TemplateView.as_view(template_name='web/reserve_0.html'), name='reserve0'),
    url(r'^reserve/1/$', TemplateView.as_view(template_name='web/reserve_1.html'), name='reserve1'),
    url(r'^reserve/2/$', TemplateView.as_view(template_name='web/reserve_2.html'), name='reserve2'),
    url(r'^reserve/3/$', TemplateView.as_view(template_name='web/reserve_3.html'), name='reserve3'),
    url(r'^reserve/4/$', TemplateView.as_view(template_name='web/reserve_4.html'), name='reserve4'),
    url(r'^reserve/5/$', TemplateView.as_view(template_name='web/reserve_5.html'), name='reserve5'),
    url(r'^signup/1/$', TemplateView.as_view(template_name='web/signup_1.html'), name='signup1'),
    url(r'^signup/2/$', TemplateView.as_view(template_name='web/signup_2.html'), name='signup2'),
    url(r'^signup/3/$', TemplateView.as_view(template_name='web/signup_3.html'), name='signup3'),
    url(r'^signup/4/$', TemplateView.as_view(template_name='web/signup_4.html'), name='signup4'),
)
