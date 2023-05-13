from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models
from django.core.validators import RegexValidator


states = (
    ('', ''),
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming'),
)
country = (('',''),('U.S', 'United States'))


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(min_length=1, max_length=20, error_messages={'required': 'First Name is required'})
    last_name = forms.CharField(min_length=1, max_length=20, error_messages={'required':'Last Name is required'})
    email = forms.EmailField(error_messages={'required':'Valid email is required'})


    class Meta (UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name','email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.CustomerProfile
        fields = ['name', 'address', 'phone', 'state', 'country', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'address': forms.TextInput(attrs={'required': True}),
            'state': forms.Select(attrs={'required': True, 'size': 0}, choices=states),
            'country': forms.Select(attrs={'required': True}, choices=country),
            'zipcode': forms.TextInput(attrs={'required': True}),
        }



