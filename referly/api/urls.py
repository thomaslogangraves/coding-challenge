from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^referrals/$', views.referral_list),
    url(r'^referrals/(?P<pk>[0-9]+)/$', views.referral_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
