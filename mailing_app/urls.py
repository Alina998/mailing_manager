from django.urls import path
from .views import HomeView, ContactsView, MailingInfoView, AddRecipientView, AddLetterView, AddMailingView
from mailing_app.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('mailings/<int:pk>/', MailingInfoView.as_view(), name='mailing_info'),
    path('add_recipient/', AddRecipientView.as_view(), name='add_recipient'),
    path('add_letter/', AddLetterView.as_view(), name='add_letter'),
    path('add_mailing/', AddMailingView.as_view(), name='add_mailing'),
]