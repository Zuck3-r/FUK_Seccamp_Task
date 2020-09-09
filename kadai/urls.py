from django.contrib import admin
from django.urls import include, path

from django.views.generic.base import RedirectView

urlpatterns = [
    path('mycalc/', include('mycalc.urls')),
    path('', RedirectView.as_view(url='/mycalc/')),
    path('admin/', admin.site.urls),
]