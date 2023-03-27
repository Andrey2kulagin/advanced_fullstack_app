from django import forms
from .models import Candidate
from django.core.validators import RegexValidator


class LowerCase(forms.CharField):
    def to_python(self, value):
        return value.lower()


class UpperCase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class NameSurName(forms.CharField):
    def to_python(self, value):
        value = value[1:].lower()
        first_sign = value[0].upper()
        return first_sign+value


class CandidateForm(forms.ModelForm):
    first_name = NameSurName(label="Имя", min_length=3, max_length=50,
                                 validators=[RegexValidator(r'^[a-zA-ZА-я\s]*$', message="Разрешены только буквы")],
                                 widget=forms.TextInput(attrs={"placeholder": "Ваше имя"}))
    last_name = NameSurName(label="Фамилия", min_length=3, max_length=50,
                                validators=[RegexValidator(r'^[a-zA-ZА-я\s]*$', message="Разрешены только буквы")],
                                widget=forms.TextInput(attrs={"placeholder": "Ваша фамилия"}))
    email = LowerCase(label="Адрес электронной почты", min_length=5, max_length=50,
                      validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
                                                 message="Вставьте настоящий адрес электронной почты")],
                      widget=forms.TextInput(attrs={"placeholder": "Ваш адрес электронной почты"}))
    age = forms.CharField(label="Возраст",
                          validators=[RegexValidator(r'^[0-9]*$', message="Разрешены только цифры до 1000")],
                          widget=forms.TextInput(attrs={"placeholder": "Ваш возраст"}))

    message = forms.CharField(label="О вас", min_length=50,
                              required=False,
                              widget=forms.Textarea(
                                  attrs={"placeholder": "Расскажите работодателям о себе", "rows": 10}))
    job = UpperCase(
        label="Код вакансии",
        min_length=5,
        max_length=5,
        widget=forms.TextInput(attrs={
            "placeholder": "Пример: FR-22",

        })
    )

    class Meta:
        model = Candidate
        fields = [
            "first_name",
            "last_name",
            "email",
            "message",
            "age",
            "phone_number",
            "job",
        ]
        widgets = {
            "phone_number": forms.TextInput(
                attrs={
                    "style": 'font-size: 13px;',
                    "placeholder": "Оставьте ваш номер телефона",
                    "data-mask": "(+7)-000-000 00 00"
                })

        }
