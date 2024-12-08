from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cap.views import SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cap.urls')), 
    path('payments/', include('payment.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('capital/signup/', SignUpView.as_view(), name='signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
