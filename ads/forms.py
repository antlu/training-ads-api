from django import forms

from ads.models import Advertisement


class AdForm(forms.ModelForm):
    """An Advertisement form for use in admin."""

    class Meta(object):
        model = Advertisement
        fields = '__all__'
        widgets = {
            'description': forms.Textarea,
        }
