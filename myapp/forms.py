from django import forms
from .models import CustomUser

class MyCustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'subject', 'message']
        exclude = ['first_name', 'last_name']      

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Name', 'labels':''}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter Your Email Address', 'labels':''}),
            'subject': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Your Subject', 'labels':''}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Your Message', 'labels':''}),

        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

       # Remove colons from labels
        # for field_name, field in self.fields.items():
        #     field.labels=''
        #     field.label_suffix = ''
        #     field.widget.attrs['class'] = 'form-control'

        

