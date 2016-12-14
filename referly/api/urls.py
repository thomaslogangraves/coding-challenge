from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Referrals API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'referrals', views.ReferralViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    url('^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
