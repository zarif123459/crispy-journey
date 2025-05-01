from django import forms
from .models import User

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first','last','username','email','password','balance']
        labels = {'first': 'First Name','last': 'Last Name','username':'Username','email': 'Email','password':'Password','balance':'Balance'}
        widgets={'first': forms.TextInput(attrs={'placeholder':'John', 'class':'form-control'}),
                 'last': forms.TextInput(attrs={'placeholder':'Appleseed', 'class':'form-control'}),
                 'username': forms.TextInput(attrs={'placeholder':'johnseeda', 'class':'form-control'}),
                 'email': forms.TextInput(attrs={'placeholder':'John@gmail.com', 'class':'form-control'}),
                 'password': forms.TextInput(attrs={'placeholder':'****', 'class':'form-control'}),
                 'balance': forms.NumberInput(attrs={'placeholder':'1000', 'class':'form-control'})
                 }
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)