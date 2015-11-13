from django.conf.urls import patterns, url, include

from thinkster_django_angular_boilerplate.views import IndexView

from rest_framework_nested import routers

from authentication.views import AccountViewSet
from authentication.views import LoginView, LogoutView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
     '',
    # ... URLs

    # connect API urls
    url(r'^api/v1/', include(router.urls)),

    # Log in and out
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),

    # Send everything else to the index (Angular to take over)
    url('^.*$', IndexView.as_view(), name='index'),
)
