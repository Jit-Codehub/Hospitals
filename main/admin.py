from django.contrib import admin
from .models import *

admin.site.register(Currency)
admin.site.register(KnowsLanguage)


from django.forms import TextInput
class OpeningHoursInline(admin.TabularInline):
    model = OpeningHours
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'timing':
            kwargs['widget'] = TextInput(attrs={'size': '8'})
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AvailableServiceInline(admin.StackedInline):
    model = AvailableService
    extra = 0

class AdressInline(admin.StackedInline):
    model = Adress
    extra = 0

class GeoInline(admin.StackedInline):
    model = Geo
    extra = 0

class AreaServedInline(admin.StackedInline):
    model = AreaServed
    extra = 0

class ContactPointInline(admin.StackedInline):
    model = ContactPoint
    extra = 0

class EmployeeInline(admin.StackedInline):
    model = Employee
    extra = 0

class ImageInline(admin.StackedInline):
    model = Image
    extra = 0

class BusinessAdmin(admin.ModelAdmin):
    list_display = ["type", "map_id", "additional_Type"] 
    inlines = [AvailableServiceInline,OpeningHoursInline,AdressInline,GeoInline,AreaServedInline,ContactPointInline,EmployeeInline,ImageInline]

admin.site.register(Business, BusinessAdmin)


class HaspartInline(admin.StackedInline):
    model = Haspart
    extra = 0

class WebsiteAdmin(admin.ModelAdmin):
    inlines = [HaspartInline,]

admin.site.register(Website, WebsiteAdmin)














