from django import forms
from .models import members,premiers,ran


class membershipForm(forms.ModelForm):
    class Meta:
        model = members
        fields = ["first_name","email","last_name","phone_number"]
class ranForm(forms.ModelForm):
    class Meta:
        model = ran
        fields = ["id_num"]

    def clean(self):
        super(ranForm, self).clean()

        id_num = self.cleaned_data_get('id_num')
