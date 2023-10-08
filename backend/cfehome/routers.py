from products.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"products-abc", ProductViewSet, basename="products")

urlpatterns = router.urls
