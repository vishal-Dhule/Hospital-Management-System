from django import forms
from .models import BillingQuery

class BillingQueryForm(forms.ModelForm):
    class Meta:
        model = BillingQuery
        fields = "__all__"

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your email"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your phone number"
            }),
            "issue": forms.Select(attrs={
                "class": "form-select"
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Describe your issue"
            }),
        }