from django.shortcuts import render,HttpResponse
from .models import *

def home(request):
    obj = Business.objects.all()[0]
    context = {"obj":obj}

    business = Business.objects.prefetch_related('curreny_Accepted', 'knows_language', 'haspart_set', 'availableservice_set', 'openinghours_set', 'adress_set', 'geo_set', 'areaserved_set', 'contactpoint_set', 'employee_set', 'image_set').get(id=1)

    # access related fields
    print(business.name)
    print(business.medical_Specialty)

    for i in business.curreny_Accepted.all():
        print(i)
    for i in business.knows_language.all():
        print(i)
    for i in business.availableservice_set.all():
        print(i)
    for i in business.openinghours_set.all():
        print(i)
    for i in business.adress_set.all():
        print(i)
    for i in business.geo_set.all():
        print(i)
    for i in business.areaserved_set.all():
        print(i)
    for i in business.contactpoint_set.all():
        print(i)
    for i in business.employee_set.all():
        print(i)
    for i in business.image_set.all():
        print(i)
    for i in business.haspart_set.all():
        print(i)
    # print(business.curreny_Accepted.all())
    # print(business.knows_language.all())
    # print(business.haspart_set.all())
    # print(business.availableservice_set.all())
    # print(business.openinghours_set.all())
    # print(business.adress_set.all())
    # print(business.geo_set.all())
    # print(business.areaserved_set.all())
    # print(business.contactpoint_set.all())
    # print(business.employee_set.all())
    # print(business.image_set.all())
    return render(request,"home.html",context)



# business = Business.objects.select_related('medical_specialty').prefetch_related('currency_accepted', 'knows_language', 'haspart_set', 'availableservice_set', 'openinghours_set', 'adress_set', 'geo_set', 'areaserved_set', 'contactpoint_set', 'employee_set', 'image_set').get(id=1)

# # access related fields
# print(business.name)
# print(business.medical_specialty)
# print(business.currency_accepted.all())
# print(business.knows_language.all())
# print(business.haspart_set.all())
# print(business.availableservice_set.all())
# print(business.openinghours_set.all())
# print(business.adress_set.all())
# print(business.geo_set.all())
# print(business.areaserved_set.all())
# print(business.contactpoint_set.all())
# print(business.employee_set.all())
# print(business.image_set.all())
