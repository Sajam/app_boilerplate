from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
import apps.page.views
import apps.party.views

router = routers.DefaultRouter()
router.register(r'party', apps.party.views.PartyViewSet)

urlpatterns = [
    url(r'^$', apps.page.views.PageView.as_view(), {'slug': 'hello_world'}, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^page/', include('backend.apps.page.urls')),
    url(r'^party/', include('backend.apps.party.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

