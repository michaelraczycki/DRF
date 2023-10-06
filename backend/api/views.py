from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    print(serializer.data)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(serializer.errors)
