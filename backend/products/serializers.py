from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "content",
            "price",
            "my_discount",
        ]

    def get_my_discount(self, obj):
        try:
            print("Obj type:", type(obj))
            return obj.get_discount()
        except:
            return None
