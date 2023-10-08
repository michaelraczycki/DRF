from products.viewset import ProductGenericViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products-abc", ProductGenericViewSet, basename="products")

urlpatterns = router.urls
