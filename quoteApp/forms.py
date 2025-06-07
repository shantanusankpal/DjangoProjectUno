from django import forms
from quoteApp.models import Quote


class QuoteAddForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = "__all__"
        widgets = {
            "quote": forms.Textarea(attrs={"rows": 3}),
        }
