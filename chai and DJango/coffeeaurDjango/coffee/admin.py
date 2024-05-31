#kisi bhi model ko add krskte hai and register kr skte!!
from django.contrib import admin
from .models import coffee_varieties, coffee_review, Store_Name, coff_certificates

# Register your models here.

class CoffeeReviewInline(admin.TabularInline):
    model=coffee_review
    extra=2


class CoffeeVarietiesAdmin(admin.ModelAdmin):
    list_display=('name', 'type', 'date')
    inlines=[CoffeeReviewInline]

class StoreNameAdmin(admin.ModelAdmin):
    list_display=['name', 'location']
    filter_horizontal=('coff_varieties', )

class CoffeeCertificatesAdmin(admin.ModelAdmin):
    list_display=['certificate_number', 'issed_date', 'valid_till']




admin.site.register(coffee_varieties, CoffeeVarietiesAdmin)
admin.site.register(coff_certificates, CoffeeCertificatesAdmin)
admin.site.register(Store_Name, StoreNameAdmin)
# admin.site.register(coffee_review, CoffeeReviewInline)

