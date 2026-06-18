from rest_framework.routers import DefaultRouter
from producto.api.views import  ProductoVewSet

router = DefaultRouter()
router.register('producto', ProductoVewSet, basename='producto')
urlpatterns = router.urls