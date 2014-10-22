from django.contrib import admin
from mine.models import Category, Page, UserProfile, User, Experiment, Locality, Field, Taxonomy, Passport, Source, Location, Stock, StockPacket

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
    list_filter = ('is_staff', 'is_superuser')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'phone', 'organization', 'job_title', 'notes', 'website', 'picture')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
