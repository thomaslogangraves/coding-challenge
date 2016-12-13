from django.conf.urls import patterns, urls

urlpatterns = patterns(
    'api.views',
    url(r'^referrals/$', 'referral_list', name='referral_list'),
    url(r'^referrals/(?P<pk>[0-9]+)$', 'referral_detail', name='referral_detail'),
)
