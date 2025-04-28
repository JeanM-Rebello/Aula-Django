from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from app_accounts.models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'cellphone', 'cpf']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Aplica 'form-control' a todos os campos do formulário
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não coincidem.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        })
    )
    password = forms.CharField(label="Senha", 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
