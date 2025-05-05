from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'mobile_number', 'address', 'message')
    search_fields = ('name', 'email', 'mobile_number')
    list_filter = ('email',)
