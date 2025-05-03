from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Managerium API",
        default_version='v1',
        description="API documentation for Managerium project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication via session (if using djoser for registration/login/logout)
    path('api/auth/', include('djoser.urls')),

    # Add DRF login/logout views (for browsable API)
    path('api-auth/', include('rest_framework.urls')),

    # App URLs
    path('api/users/', include('users.urls')),
    path('api/rooms/', include('rooms.urls')),
    path('api/hotel/', include('hotel.urls')),
    path('api/reservations/', include('reservations.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/maintenance/', include('maintenance.urls')),
    path('api/billing/', include('billing.urls')),

    # API Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
