from .views import ListingViewSet, BookingViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router = router.register('listings', ListingViewSet)
router = router.register('bookings', BookingViewSet)

urlpatterns = router.urls
