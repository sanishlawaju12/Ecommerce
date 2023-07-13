from django import forms

from . import models

class CategoryForm(forms.ModelForm):

    class Meta:
        model = models.Category
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )

class CustomerForm(forms.ModelForm):

    class Meta:
        model = models.Customer
        exclude = []

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class' : 'form-control',
                }
            )


class OrderForm(forms.ModelForm):

    class Meta:
        model = models.Order
        exclude = []
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class' : 'form-control',
                }
            )


class CartForm(forms.ModelForm):

    class Meta:
        model = models.Cart
        exclude = []
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class' : 'form-control',
                }
            )


