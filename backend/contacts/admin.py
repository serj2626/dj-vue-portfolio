from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact)'''

    list_display = ('name', 'email', 'message', 'created_at')
