from django.forms import ModelForm

from mailing_app.models import Letter, Mailing, Recipient


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = ["email", "name", "comment"]

    def __init__(self, *args, **kwargs):
        super(RecipientForm, self).__init__(*args, **kwargs)

        self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "Введите email получателя"})

        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Введите ФИО получателя"})

        self.fields["comment"].widget.attrs.update({"class": "form-control", "placeholder": "Укажите комментарий"})

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Recipient.objects.filter(email=email).exists():
            self.add_error("email", "Эта почта уже зарегистрирована")
        return email


class LetterForm(ModelForm):
    class Meta:
        model = Letter
        fields = ["subject", "letter"]

    def __init__(self, *args, **kwargs):
        super(LetterForm, self).__init__(*args, **kwargs)

        self.fields["subject"].widget.attrs.update({"class": "form-control", "placeholder": "Введите тему письма"})

        self.fields["letter"].widget.attrs.update({"class": "form-control", "placeholder": "Поле для письма"})


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ["status", "letter", "recipient_list", "owner"]

    def __init__(self, *args, **kwargs):
        super(MailingForm, self).__init__(*args, **kwargs)

        self.fields["status"].widget.attrs.update({"class": "form-select", "placeholder": "Выберите статус рассылки"})

        self.fields["letter"].widget.attrs.update({"class": "form-control", "placeholder": "Поле для письма"})

        self.fields["recipient_list"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите получателей"}
        )

        self.fields["owner"].widget.attrs.update({"class": "form-control", "placeholder": "Автор"})
