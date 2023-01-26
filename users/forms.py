from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Bino',
            }
        ),
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )


class SignupForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Bino Nunes dos Reis',
            }
        ),
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: bino@email.com',
            }
        ),
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Xpto123',
            }
        ),
    )
    password_confirmation = forms.CharField(
        label='Confirmação de senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Xpto123',
            }
        ),
    )
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if username:
            username = username.strip()
            
            if ' ' in username:
                raise forms.ValidationError('O campo username não pode conter espaços')
            else:
                return username

    def clean_password_confirmation(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        
        if password and password_confirmation:
            if password != password_confirmation:
                raise forms.ValidationError('As senhas precisam ser iguais!')
            else:
                return password
