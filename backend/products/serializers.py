from products.models import Product
from rest_framework import serializers
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    email = serializers.EmailField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = [
            "url",
            "edit_url",
            "email",
            "pk",
            "id",
            "title",
            "content",
            "price",
            "my_discount",
        ]

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        try:
            print("Obj type:", type(obj))
            return obj.get_discount()
        except:
            return None
