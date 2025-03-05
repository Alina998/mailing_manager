from django.urls import path

from mailing_app.apps import MailingAppConfig
from mailing_app.services import send_mailing

from .views import (
    ContactsView,
    HomeView,
    LetterCreateView,
    LetterDeleteView,
    LetterInfoView,
    LetterUpdateView,
    MailingCreateView,
    MailingDeleteView,
    MailingInfoView,
    MailingUpdateView,
    RecipientCreateView,
    RecipientDeleteView,
    RecipientInfoView,
    RecipientUpdateView,
)

app_name = MailingAppConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("mailings/<int:pk>/", MailingInfoView.as_view(), name="mailing_info"),
    path("recipient/<int:pk>/", RecipientInfoView.as_view(), name="recipient_info"),
    path("recipient/add/", RecipientCreateView.as_view(), name="add_recipient"),
    path("recipient/<int:pk>/", RecipientUpdateView.as_view(), name="update_recipient"),
    path("recipient/<int:pk>/delete/", RecipientDeleteView.as_view(), name="delete_recipient"),
    path("letter/<int:pk>/", LetterInfoView.as_view(), name="letter_info"),
    path("letter/add/", LetterCreateView.as_view(), name="add_letter"),
    path("letter/<int:pk>/", LetterUpdateView.as_view(), name="update_letter"),
    path("letter/<int:pk>/delete/", LetterDeleteView.as_view(), name="delete_letter"),
    path("mailing/<int:pk>/", MailingInfoView.as_view(), name="mailing_info"),
    path("mailing/add/", MailingCreateView.as_view(), name="add_mailing"),
    path("mailing/<int:pk>/", MailingUpdateView.as_view(), name="update_mailing"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="delete_mailing"),
    path("mailing/start/<int:mailing_id>/", send_mailing, name="send_mailing"),
]
