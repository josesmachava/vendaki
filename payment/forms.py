from django import forms

from .models import Payment


class PaymentForm(forms.ModelForm):
    name = forms.CharField(label="Nome completo", widget=forms.TextInput(attrs={'placeholder': 'Nome completo'}),
                                max_length=30, required=True)
    número_de_telefone = forms.CharField(label="Digite o seu 84 xxxx", widget=forms.TextInput(attrs={'placeholder': 'Digite o seu 84 xxxx'}),
                               max_length=30, required=False)

    class Meta:
        model = Payment
        fields = ('name', 'número_de_telefone')
