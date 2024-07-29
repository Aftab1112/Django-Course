from django.contrib import admin
from .models import Chai_Variety,Chai_Reviews,Store,Chai_Certificate

# Register your models here.

class Chai_Review_Inline(admin.TabularInline):
    model = Chai_Reviews
    extra = 2

class Chai_Variety_Admin(admin.ModelAdmin):
    list_display = ("name","type","date_added")
    inlines = [Chai_Review_Inline]
    
class Store_Admin(admin.ModelAdmin):
    list_display = ("name","location")
    filter_horizontal = ("chai_varieties",)

class Chai_Certificate_Admin(admin.ModelAdmin):
    list_display = ("chai","certificate_number")

admin.site.register(Chai_Variety,Chai_Variety_Admin)
admin.site.register(Store,Store_Admin)
admin.site.register(Chai_Certificate,Chai_Certificate_Admin)
