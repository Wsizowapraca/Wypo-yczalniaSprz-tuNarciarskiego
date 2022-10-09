from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class RentForm(forms.Form):
    phone = forms.CharField(label='phone', max_length=12)
    email = forms.EmailField(label='email', max_length=254)
    enddate = forms.DateTimeField(label='enddate')

# class ChangePassword(forms.Form):
#     newpassword = forms.CharField(label='newpassword', max_length=30)
#     confirmnewpassword = forms.CharField(label='confirmnewpassword', max_length=30)

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=150)
    password = forms.CharField(label='password', max_length=128, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=150)
    typeEmailX = forms.EmailField(label='typeEmailX', max_length=254)
    typePasswordX = forms.CharField(label='typePasswordX', max_length=128, widget=forms.PasswordInput)
    # confirm_password = forms.CharField(label='typePasswordX', max_length=128, widget=forms.PasswordInput)