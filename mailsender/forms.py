from django import forms

from mailsender.models import Mailing, MailText, Customer


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['status']
        widgets = {
            'mailing_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class MailTextForm(forms.ModelForm):
    class Meta:
        model = MailText
        fields = ['topic', 'message']


class CustomerForm(forms.ModelForm):
    """
    Класс формы клиента для вьюхи MailingManagementCreateView
    """

    class Meta:
        model = Customer
        fields = []

    existing_customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),  # Запрос для получения всех клиентов
        required=False,  # Поле необязательное
        empty_label="Выберите клиентов",  # Текст для пустого значения
        label="Клиент"  # Текст для поля
    )


class CustomerCreateForm(forms.ModelForm):
    """
    Класс формы клиента для вьюхи CustomersCreateView
    """

    class Meta:
        model = Customer
        fields = ['last_name','first_name', 'middle_name', 'email']
