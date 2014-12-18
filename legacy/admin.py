from django.contrib import admin
from legacy.models import Legacy_Seed, Legacy_Row

class Legacy_SeedAdmin(admin.ModelAdmin):
  list_display = ('seed_id', 'seed_name')

class Legacy_RowAdmin(admin.ModelAdmin):
  list_display = ('row_id', 'pedigree')

admin.site.register(Legacy_Seed, Legacy_SeedAdmin)
admin.site.register(Legacy_Row, Legacy_RowAdmin)
