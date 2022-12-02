
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import CarView,BookingRequestView
router=DefaultRouter()
router.register('cars',viewset=CarView,basename="car")
router.register('booking_requests',viewset=BookingRequestView,basename="requests")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/user/',include('app.urls')),
    path('app/',include(router.urls))
]
