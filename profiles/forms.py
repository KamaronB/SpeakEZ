from django.forms import ModelForm
from .models import User,Profile




class InfoForm(ModelForm):
    class Meta:
        model= Profile
        fields=['bio','location','birth_date']
    # bio = forms.CharField(label='Bio', max_length=500)
    # location = forms.CharField(label='Location', max_length=30)
    # birth = forms.DateField(label='Date of Birth')
