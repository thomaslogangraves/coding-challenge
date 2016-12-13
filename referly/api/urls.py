from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^referrals/$', views.referral_list),
    url(r'^referrals/(?P<pk>[0-9]+)/$', views.referral_detail),
]
