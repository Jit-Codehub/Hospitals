from django.contrib import admin
from .models import *
from django.template.loader import get_template
from django import forms

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

class HaspartInline(admin.StackedInline):
    model = Haspart
    extra = 0

class BusinessAdmin(admin.ModelAdmin):
    fields = ["type",'map_id','additional_Type','Avail','medical_Specialty','curreny_Accepted','Open','payment_Accepted','Adress','Geo','hasMap','logo','telephone','isAcceptingNewPatients','AreaServed','ContactPoint','Employee','knows_language','Image','url','name','AlternateName','description','disambiguatingDescription','foundingDate','SameAs','pub_type','publisher_id','pub_name','website_id','pub_url','Has',]
  

    inlines = [AvailableServiceInline,OpeningHoursInline,AdressInline,GeoInline,AreaServedInline,ContactPointInline,EmployeeInline,ImageInline,HaspartInline]
    readonly_fields = ('Avail','Open','Adress','Geo','AreaServed','ContactPoint','Employee','Image','Has',) 

    def Avail(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)
    
    def Open(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)
    
    def Adress(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)
    
    def Geo(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)
    
    def AreaServed(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)
    
    def ContactPoint(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)
    
    def Employee(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)
    
    def Image(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)
    
    def Has(self, *args, **kwargs):
        context = getattr(self.response, 'context_data', None) or {}
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
        return get_template(inline.opts.template).render(context, self.request)

    def render_change_form(self, request, *args, **kwargs):
        self.request = request
        self.response = super().render_change_form(request, *args, **kwargs)
        return self.response
    
    

admin.site.register(Business, BusinessAdmin)
