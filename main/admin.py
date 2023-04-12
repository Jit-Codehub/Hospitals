from django.contrib import admin
from .models import *
from django.template.loader import get_template
from django import forms

admin.site.register(Currency)
admin.site.register(KnowsLanguage)


from django.forms import TextInput
class OpeningHoursInline(admin.TabularInline):
    insert_after = 'curreny_Accepted'
    model = OpeningHours
    extra = 0

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'timing':
            kwargs['widget'] = TextInput(attrs={'size': '8'})
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class AvailableServiceInline(admin.StackedInline):
    insert_after = 'additional_Type'
    model = AvailableService
    extra = 0

class AdressInline(admin.StackedInline):
    insert_after = 'payment_Accepted'
    model = Adress
    extra = 0

class GeoInline(admin.StackedInline):
    insert_after = 'payment_Accepted'

    model = Geo
    extra = 0

class AreaServedInline(admin.StackedInline):
    insert_after = 'isAcceptingNewPatients'

    model = AreaServed
    extra = 0

class ContactPointInline(admin.StackedInline):
    insert_after = 'isAcceptingNewPatients'

    model = ContactPoint
    extra = 0

class EmployeeInline(admin.StackedInline):
    insert_after = 'isAcceptingNewPatients'

    model = Employee
    extra = 0

class ImageInline(admin.StackedInline):
    insert_after = 'knows_language'

    model = Image
    extra = 0

class HaspartInline(admin.StackedInline):
    insert_after = 'pub_url'

    model = Haspart
    extra = 0

class BusinessAdmin(admin.ModelAdmin):
    fields = ["type",'map_id','additional_Type','medical_Specialty','curreny_Accepted',"payment_Accepted","hasMap","logo","telephone","isAcceptingNewPatients","knows_language","url","name","AlternateName","description","disambiguatingDescription","foundingDate","SameAs","pub_type","publisher_id","pub_name","website_id","pub_url"]

    inlines = [AvailableServiceInline,OpeningHoursInline,AdressInline,GeoInline,AreaServedInline,ContactPointInline,EmployeeInline,ImageInline,HaspartInline]

    change_form_template = 'admin/custom/change_form.html'
    class Media:
        css = {
            'all': (
                'css/admin.css',
            )
        }
   
admin.site.register(Business, BusinessAdmin)
