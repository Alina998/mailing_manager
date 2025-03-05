from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, TemplateView, UpdateView

from .forms import LetterForm, MailingForm, RecipientForm
from .models import Letter, Mailing, Recipient


class HomeView(ListView):
    model = Mailing
    template_name = "home.html"
    context_object_name = "mailings"

    def get_queryset(self):
        queryset = cache.get("authors_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("authors_queryset", queryset, 60 * 15)  # Кешируем данные на 15 минут
        return queryset


@method_decorator(cache_page(60 * 15), name="dispatch")
class MailingInfoView(DetailView):
    model = Mailing
    template_name = "mailing_info.html"
    context_object_name = "mailing"


@method_decorator(cache_page(60 * 15), name="dispatch")
class ContactsView(TemplateView):
    template_name = "contacts.html"

    def post(self, request, *args, **kwargs):
        return self.render_to_response({"success": True})


@method_decorator(cache_page(60 * 15), name="dispatch")
class RecipientInfoView(DetailView):
    model = Recipient
    template_name = "recipient_info.html"
    context_object_name = "recipient"


class RecipientCreateView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    model = Recipient
    form_class = RecipientForm
    template_name = "add_recipient.html"
    permission_required = "mailing_app.add_recipient"

    def get_success_url(self):
        return reverse("mailing_app:recipient_info", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Recipient
    form_class = RecipientForm
    template_name = "update_recipient.html"
    permission_required = "mailing_app.change_recipient"

    def form_valid(self, form):
        return super().form_valid(form)

    def handle_no_permission(self):
        return super().handle_no_permission()

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner

    def get_success_url(self):
        return reverse("mailing_app:recipient_info", kwargs={"pk": self.object.pk})


class RecipientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Recipient
    form_class = RecipientForm
    template_name = "delete_recipient.html"
    success_url = reverse_lazy("home")
    permission_required = "mailing_app.delete_recipient"

    def handle_no_permission(self):
        return super().handle_no_permission()

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner


@method_decorator(cache_page(60 * 15), name="dispatch")
class LetterInfoView(DetailView):
    model = Letter
    template_name = "letter_info.html"
    context_object_name = "letter"


class LetterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Letter
    form_class = LetterForm
    template_name = "add_letter.html"
    permission_required = "mailing_app.add_letter"

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("mailing_app:letter_info", kwargs={"pk": self.object.pk})


class LetterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Letter
    form_class = LetterForm
    template_name = "update_letter.html"
    permission_required = "mailing_app.change_letter"

    def form_valid(self, form):
        return super().form_valid(form)

    def handle_no_permission(self):
        return super().handle_no_permission()

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner

    def get_success_url(self):
        return reverse("mailing_app:letter_info", kwargs={"pk": self.object.pk})


class LetterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Letter
    form_class = LetterForm
    template_name = "delete_letter.html"
    success_url = reverse_lazy("home")
    permission_required = "mailing_app.delete_letter"

    def handle_no_permission(self):
        return super().handle_no_permission()

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = "add_mailing.html"
    permission_required = "mailing_app.add_mailing"

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("mailing_app:mailing_info", kwargs={"pk": self.object.pk})


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = "update_mailing.html"
    permission_required = "mailing_app.change_mailing"

    def form_valid(self, form):
        return super().form_valid(form)

    def handle_no_permission(self):
        return super().handle_no_permission()

    def get_success_url(self):
        return reverse("mailing_app:mailing_info", kwargs={"pk": self.object.pk})


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    form_class = MailingForm
    template_name = "delete_mailing.html"
    success_url = reverse_lazy("home")
    permission_required = "mailing_app.delete_mailing"

    def handle_no_permission(self):
        return super().handle_no_permission()

    def test_func(self):
        mailing = self.get_object()
        return self.request.user == mailing.owner
