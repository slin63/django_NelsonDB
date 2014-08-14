from django.contrib import admin
from legacy.models import Seed, Row

class SeedAdmin(admin.ModelAdmin):
  list_display = ('seed_id', 'seed_name')

class RowAdmin(admin.ModelAdmin):
  list_display = ('row_id', 'pedigree')

admin.site.register(Seed, SeedAdmin)
admin.site.register(Row, RowAdmin)
