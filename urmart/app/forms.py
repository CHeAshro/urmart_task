
from django import forms
from django.forms.models import ModelForm, ModelChoiceField
from app.models import Order, Product


class BaseModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 附加 bootstrap class
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'


class CreateOrderForm(BaseModelForm):

    product = ModelChoiceField(queryset=Product.objects.all(), empty_label='Select Product')

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'qty': forms.NumberInput(attrs={'placeholder': '數量'}),
            'customer_id': forms.NumberInput(attrs={'placeholder': 'Customer ID'}),
        }
