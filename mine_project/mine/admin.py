from django.contrib import admin
from mine.models import Category, Page, UserProfile, User, Experiment, Locality, Field, Taxonomy, AccessionCollecting, Passport, Source, Location, Stock, StockPacket

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url', 'views')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'views', 'likes')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
    list_filter = ('is_staff', 'is_superuser')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'phone', 'organization', 'job_title', 'notes', 'website', 'picture')

class ExperimentAdmin(admin.ModelAdmin):
	list_display = ('name', 'start_date', 'user', 'factor', 'purpose', 'comments')
	list_filter = ('name', 'start_date')

class LocalityAdmin(admin.ModelAdmin):
	list_display = ('city', 'state', 'country', 'zipcode')
	list_filter = ('city', 'country')

class FieldAdmin(admin.ModelAdmin):
	list_display = ('locality', 'field_name', 'field_number', 'latitude', 'longitude', 'comments')

class TaxonomyAdmin(admin.ModelAdmin):
	list_display = ('genus', 'species', 'subspecies', 'population', 'common_name')

class AccessionCollectingAdmin(admin.ModelAdmin):
	list_display = ('field', 'user', 'collection_date', 'collection_number', 'collection_method', 'comments')

class SourceAdmin(admin.ModelAdmin):
	list_display = ('source_name')

class PassportAdmin(admin.ModelAdmin):
	list_display = ('id', 'accession_collecting', 'source', 'taxonomy', 'pedigree')

class LocationAdmin(admin.ModelAdmin):
	list_display = ('locality', 'building_name', 'room', 'section', 'column', 'shelf', 'box_name')

class StockAdmin(admin.ModelAdmin):
	list_display = ('id', 'passport', 'source_tagname', 'stock_name', 'cross_type', 'bulk_type', 'stock_status', 'stock_date')

class StockPacketAdmin(admin.ModelAdmin):
	list_display = ('barcode', 'stock', 'location', 'weight', 'num_seeds', 'comments')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Experiment, ExperimentAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(AccessionCollecting, AccessionCollectingAdmin)
admin.site.register(Passport, PassportAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(StockPacket, StockPacketAdmin)
