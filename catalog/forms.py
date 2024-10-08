from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'description', 'product_image', 'category', 'unit_price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        if cleaned_data.lower() in ('казино', 'криптовалюта', 'крипта',
            'биржа', 'дешево', 'бесплатно', 'обман',
            'полиция', 'радар'):
            raise forms.ValidationError('Недопустимые слова в названии')

        return cleaned_data