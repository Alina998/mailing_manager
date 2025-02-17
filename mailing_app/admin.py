from django.contrib import admin
from .models import Recipient, Letter

class RecipientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'comment')

class LetterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'letter')
    search_fields = ('subject', 'letter')

admin.site.register(Recipient, RecipientAdmin)
admin.site.register(Letter, LetterAdmin)
