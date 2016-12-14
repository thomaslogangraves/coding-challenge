from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^referrals/$', views.ReferralList.as_view(), name='referral-list'),
    url(r'^referrals/(?P<pk>[0-9]+)/$', views.ReferralDetail.as_view(), name='referral-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
])

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
