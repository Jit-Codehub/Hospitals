from django.shortcuts import render
from .models import *
import json

def home(request):
    business = Business.objects.prefetch_related('curreny_Accepted', 'knows_language', 'haspart_set', 'availableservice_set', 'openinghours_set', 'adress_set', 'geo_set', 'areaserved_set', 'contactpoint_set', 'employee_set', 'image_set').get(type="Physician")

    l_availableService = []
    for i in business.availableservice_set.all():
        d = {}
        if i.url:
            d['@id'] = i.url
        if i.type:
            d['@type'] = i.type
        if i.code:
            d[f'code'] = i.code
        if i.name:
            d[f'name'] = i.name
        if i.sameAs:
            d['sameAs'] = i.sameAs
        if i.description:
            d['description'] = i.description
        l_availableService.append(d)

   
    openhours = ''
    for i in business.openinghours_set.all():
        if i.day:
            openhours+=i.day+" "
        if i.timming:
            openhours+=i.timming+"  "


    l_adress = []
    for i in business.adress_set.all():
        d = {}
        if i.type:
            d['@type'] = i.type
        if i.postalCode:
            d['postalCode'] = i.postalCode
        if i.addressRegion:
            d['addressRegion'] = i.addressRegion
        if i.addressCountry:
            d['addressCountry'] = i.addressCountry
        if i.streetAddress:
            d['streetAddress'] = i.streetAddress
        if i.addressLocality:
            d['addressLocality'] = i.addressLocality
        l_adress.append(d)

    l_geo = []
    for i in business.geo_set.all():
        d = {}
        if i.type:
            d['@type'] = i.type
        if i.name:
            d['name'] = i.name
        if i.postalCode:
            d['postalCode'] = i.postalCode
        if i.latitude:
            d['latitude'] = i.latitude
        if i.longitude:
            d['longitude'] = i.longitude
        if i.description:
            d['description'] = i.description
        
        l_geo.append(d)


    l_areaServed = []
    for i in business.areaserved_set.all():
        d = {}
        if i.type:
            d['@type'] = i.type
        if i.name:
            d['name'] = i.name
        if i.url:
            d['@id'] = i.url
        
        l_areaServed.append(d)

    l_contactPoint = []
    for i in business.contactpoint_set.all():
        d = {}
        if i.type:
            d['@type'] = i.type
        if i.contactType:
            d['contactType'] = i.contactType
        if i.telephone:
            d['telephone'] = i.telephone
        if i.email:
            d['email'] = i.email
        
        l_contactPoint.append(d)


    l_employee = []
    for i in business.employee_set.all():
        d = {}
        if i.url:
            d['@id'] = i.url
        
        l_employee.append(d)

    l_image = []
    for i in business.image_set.all():
        d = {}
        if i.type:
            d['@type'] = i.type
        if i.name:
            d['name'] = i.name
        if i.url:
            d['url'] = i.url.url
        if i.creator:
            d['creator'] = i.creator
        if i.contentLocation:
            d['contentLocation'] = i.contentLocation
        
        l_image.append(d)

    l_publisher = []
    for i in business.publisher_set.all():
        d = {}
        if i.publisher_id:
            d['@id'] = i.publisher_id
        
        l_publisher.append(d)

    l_haspart = []
    for i in business.haspart_set.all():
        d = {}
        if i.type:
            d['@type'] = i.type
        if i.url:
            d['@id'] = i.url
        
        l_haspart.append(d)


    businessSchema ={
    "@context":"https://schema.org",
    "@graph":[
        {
            "@context":"https://schema.org",
            "@type":business.type,
            "@id":business.map_id,
            "additionalType":business.additional_Type,
            "availableService":l_availableService ,
          
                        "medicalSpecialty":business.medical_Specialty,
                        "currenciesAccepted":[i.currencyName for i in business.curreny_Accepted.all()],
            "openingHours":openhours,
                        "paymentAccepted":business.payment_Accepted,
            "address":l_adress,
            "geo":l_geo,                        
            "hasMap":business.hasMap,
                        "logo":business.logo.url,
                        "telephone":business.telephone,
                        "isAcceptingNewPatients":business.isAcceptingNewPatients,
                        "areaServed":l_areaServed,
            "contactPoint":l_contactPoint,
                        "employee":l_employee,
                        "knowsLanguage":[i.language for i in business.knows_language.all()],
            "image":l_image,
            "url":business.url,
            "name":business.name,
            "alternateName":[business.AlternateName],
            "description":business.description,
            "disambiguatingDescription":business.disambiguatingDescription,
            "foundingDate":business.foundingDate,
            "sameAs":[business.SameAs]
        },
        {
                        "@type":business.publisher_type,
                        "publisher":l_publisher,
                        "name":business.publisher_name,
                        "@id":business.website_id,
                        "url":business.website_url,
                        "hasPart":l_haspart,
        }
    ]
}


    business_Schema = '<script type="application/ld+json">'
    business_Schema += json.dumps(businessSchema)
    business_Schema += '</script>'
    
    #for footer
    oh = business.openinghours_set.all()
    add = business.adress_set.all()
    ct = business.contactpoint_set.all()

    context = {"businessSchema":business_Schema,"oh":oh,"add":add,"ct":ct}
    return render(request,"home.html",context)



def contact(request):

    business = Business.objects.prefetch_related('openinghours_set', 'adress_set', 'contactpoint_set',).get(type="Physician")

    #for footer
    oh = business.openinghours_set.all()
    add = business.adress_set.all()
    ct = business.contactpoint_set.all()

    # print(request)
    print(business.map_id)
    name = request.POST["name"]
    email = request.POST["email"]
    message = request.POST["message"]
    question = Question(name=name,email=email,comment=message)
    question.save()
    
    context = {"oh":oh,"add":add,"ct":ct,"map":business.map_id}
    # return render(request,"contact-us.html")
    return render(request,"contact.html",context)




