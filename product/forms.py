from django import forms
from .models import Products
class ProductSaveForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['id', 'sub_id']

    # Validation password
    def clean(self, *args, **kwargs):
        product_id = self.cleaned_data.get("id")
        substitution_id = self.cleaned_data.get("sub_id")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Cette email est déjà existant!")

        return super(ProductSaveForm, self).clean(*args, **kwargs)

