from django.contrib import admin
from models import UserLink, Account

class AccountAdmin(admin.ModelAdmin):
    search_fields=['user']

class LinkAdmin(admin.ModelAdmin):
    search_fields=['from_user']
    list_display = ('from_user', 'to_user')

admin.site.register(UserLink, LinkAdmin)
admin.site.register(Account, AccountAdmin)
