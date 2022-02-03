from django.urls import path, include
from . import views

urlpatterns = [
    path('test-endpoint', views.test_endpoint),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('cars', views.get_cars),
    path('cars/<int:pk>', views.get_car),
    path('test-tubes', views.get_test_tubes),
    path('test-tubes/<int:pk>', views.get_test_tube),
    path('collection-points', views.get_collection_points),
    path('collection-points/<int:pk>', views.get_collection_point),
]