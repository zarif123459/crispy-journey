from django import forms
from .models import User,Category,Transaction
from django.utils.timezone import now

class userForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '****',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['first', 'last', 'username', 'email', 'password', 'balance']
        labels = {
            'first': 'First Name',
            'last': 'Last Name',
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'balance': 'Balance'
        }
        widgets = {
            'first': forms.TextInput(attrs={'placeholder': 'John', 'class': 'form-control'}),
            'last': forms.TextInput(attrs={'placeholder': 'Appleseed', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'johnseeda', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'John@gmail.com', 'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'placeholder': '1000', 'class': 'form-control'})
        }

        
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','setbudget']
        labels={'name': 'Category Name','setbudget': 'Set Category Budget'}
        widgets={'name': forms.TextInput(attrs={'class': 'form-control'}),
                 'setbudget': forms.NumberInput(attrs={'class': 'form-control'})}
        
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'date']  # include 'date'

        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        labels = {
            'amount': 'Transaction Amount',
            'category': 'Category',
            'date': 'Transaction Date',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = now().date()  # default current date

class userFormAdmin(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '****',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['first', 'last', 'username', 'email', 'password', 'balance','role']
        labels = {
            'first': 'First Name',
            'last': 'Last Name',
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'balance': 'Balance',
            'role': 'Role'
        }
        widgets = {
            'first': forms.TextInput(attrs={'placeholder': 'John', 'class': 'form-control'}),
            'last': forms.TextInput(attrs={'placeholder': 'Appleseed', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'johnseeda', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'John@gmail.com', 'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'placeholder': '1000', 'class': 'form-control'}),
            'role': forms.TextInput(attrs={'placeholder': 'personal', 'class': 'form-control'}),
        }