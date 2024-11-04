"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register(r"categories", views.CategoryViewSet)
router.register(r"discount-coupon", views.DiscountCouponViewSet)
router.register(r"services", views.ServiceViewSet)
router.register(r"rooms", views.RoomViewSet)
router.register(r"bookings", views.BookingViewSet)
router.register(r"room-availability", views.RoomAvailabilityViewSet)
router.register(r"booking-service", views.BookingServiceViewSet)
router.register(r"cancellations", views.CancellationViewSet)
router.register(r"payments", views.PaymentViewSet)
router.register(r"feedbacks", views.FeedbackViewSet)
router.register(r"bookings-rooms", views.BookingRoomViewSet)
router.register(r"room-photos", views.RoomPhotoViewSet)

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/media/", include(uploader_router.urls)),
    path("check-coupon/<str:code>/", views.CheckDiscountCouponView.as_view(), name="check_coupon",),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
