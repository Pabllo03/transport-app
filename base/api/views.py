from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from base.api.serializers import CarSerializer, TestTubeSerializer, CollectionPointSerializer
from base.models import Car, TestTube, CollectionPoint

@api_view(['GET'])
@permission_classes([AllowAny])
def test_endpoint(request):
    test_response = {
        'status': '300 - 1',
        'NOT': 'ProTECteD :)'
    }
    return Response(data=test_response, status=299)


@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()

    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_car(request, pk):
    car = Car.objects.get(id=pk)

    serializer = CarSerializer(car)
    return Response(serializer.data)

@api_view(['GET'])
def get_test_tubes(request):
    test_tubes = TestTube.objects.all()

    serializer = TestTubeSerializer(test_tubes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_test_tube(request, pk):
    test_tube = TestTube.objects.get(id=pk)

    serializer = TestTubeSerializer(test_tube)
    return Response(serializer.data)

@api_view(['GET'])
def get_collection_points(request):
    collection_points = CollectionPoint.objects.all()

    serializer = CollectionPointSerializer(collection_points, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_collection_point(request, pk):
    collection_point = CollectionPoint.objects.get(id=pk)

    serializer = CollectionPointSerializer(collection_point)
    return Response(serializer.data)