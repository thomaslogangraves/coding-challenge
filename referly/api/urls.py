from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^referrals/$', views.ReferralList.as_view()),
    url(r'^referrals/(?P<pk>[0-9]+)/$', views.ReferralDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
