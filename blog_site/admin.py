from django.contrib import admin
from .models import User, Article, Comments

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'user_email', 'online_status', 'formatted_creation_date')
    list_filter = ('online_status', 'creation_date')

    def formatted_creation_date(self, obj):
        return obj.creation_date.strftime('%Y-%m-%d')
    
    formatted_creation_date.short_description = 'Creation Date'
    formatted_creation_date.admin_order_field = 'creation_date'

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Article)
admin.site.register(Comments)