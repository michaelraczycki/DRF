from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get("content")
        if len(content) < 4:
            raise forms.ValidationError("Content is too short")
        return content

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if len(title) < 4:
            raise forms.ValidationError("Title is too short")
        return title

    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price <= 1.00:
            raise forms.ValidationError("Price must be greater than $1.00")
        elif price >= 99.99:
            raise forms.ValidationError("Price must be less than $100.00")
        return price
