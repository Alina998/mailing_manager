from .models import Recipient, Letter, Mailing
from django import forms
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView


class HomeView(ListView):
    model = Mailing
    template_name = 'home.html'
    context_object_name = 'mailings'

class MailingInfoView(DetailView):
    model = Mailing
    template_name = 'mailing_info.html'
    context_object_name = 'mailing'


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        return self.render_to_response({'success': True})


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['email', 'name', 'comment']

class AddRecipientView(CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'add_recipient.html'
    success_url = '/recipient/'

    def form_valid(self, form):
        return super().form_valid(form)


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['subject', 'letter']

class AddLetterView(CreateView):
    model = Letter
    form_class = LetterForm
    template_name = 'add_letter.html'
    success_url = '/letter/'

    def form_valid(self, form):
        return super().form_valid(form)

class AddMailingView(CreateView):
    model = Mailing
    template_name = 'add_mailing.html'
    success_url = '/mailing/'
