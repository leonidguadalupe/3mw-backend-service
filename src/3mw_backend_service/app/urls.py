from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from backend.api import router
from backend.api.views import FetchMonitoringViewSet, ReportingViewSet

urlpatterns = [
    path('', include(router.urls)),
    url(r'^monitoring/$', FetchMonitoringViewSet.as_view()),
    url(r'^report/$', ReportingViewSet.as_view()),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
