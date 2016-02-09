from django.contrib import admin
from lab.models import UserProfile, User, Experiment, Locality, Field, Taxonomy, Passport, Location, Stock, StockPacket, UploadQueue

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
    list_filter = ('is_staff', 'is_superuser')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'phone', 'organization', 'job_title', 'notes', 'website', 'picture')

class ExperimentAdmin(admin.ModelAdmin):
	list_display = ('user', 'field', 'name', 'start_date', 'purpose', 'comments')

class UploadQueueAdmin(admin.ModelAdmin):
	list_display = ('experiment', 'user', 'file_name', 'upload_type', 'date', 'completed', 'comments')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UploadQueue, UploadQueueAdmin)
admin.site.register(Experiment, ExperimentAdmin)


# Test registrations
from lab.models import GlycerolStock

admin.site.register(GlycerolStock)