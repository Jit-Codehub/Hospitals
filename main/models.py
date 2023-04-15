from django.db import models

STATUS_CHOICE = (
    ("Sunday", "Sunday"),
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
)

STATUS_PATIENT = (
    ("True", "True"),
    ("False", "False"),
)

class Currency(models.Model):
    currencyName = models.CharField(max_length=255)

    def __str__(self):
        return self.currencyName
    
class KnowsLanguage(models.Model):
    language = models.CharField(max_length=255)

    def __str__(self):
        return self.language


class Business(models.Model):
    type = models.CharField(max_length=255)
    map_id = models.URLField(blank=True,null=True)
    additional_Type = models.URLField(blank=True,null=True)
    medical_Specialty = models.CharField(max_length=255,blank=True,null=True)
    curreny_Accepted = models.ManyToManyField(Currency)
    payment_Accepted = models.CharField(max_length=255,blank=True,null=True)
    hasMap = models.URLField(blank=True,null=True)
    logo = models.ImageField(upload_to='logo/',blank=True,null=True)
    telephone = models.CharField(max_length=255,blank=True,null=True)
    isAcceptingNewPatients = models.CharField(max_length=255, choices=STATUS_PATIENT,default='yes')
    knows_language = models.ManyToManyField(KnowsLanguage)
    url = models.URLField(blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    AlternateName = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    disambiguatingDescription = models.TextField(blank=True,null=True)
    foundingDate = models.CharField(max_length=255,blank=True,null=True)
    SameAs = models.TextField(blank=True,null=True)
    publisher_type = models.CharField(max_length=255,blank=True,null=True)
    publisher_name = models.CharField(max_length=100,blank=True,null=True)
    website_id = models.URLField(blank=True,null=True)
    website_url = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.type

class Publisher(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    publisher_id = models.URLField()
class Haspart(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255,blank=True,null=True)
    url = models.URLField(blank=True,null=True)
class AvailableService(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    code = models.CharField(max_length=255,blank=True,null=True)
    name = models.CharField(max_length=255)
    sameAs = models.URLField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    url = models.URLField(blank=True,null=True)

class OpeningHours(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    day = models.CharField(max_length=255, choices=STATUS_CHOICE)
    timming = models.CharField(max_length=255)

class Adress(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    addressRegion = models.CharField(max_length=255)
    addressCountry = models.CharField(max_length=255)
    streetAddress = models.CharField(max_length=500)
    addressLocality = models.CharField(max_length=500)

class Geo(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    postalCode = models.CharField(max_length=255,blank=True,null=True)
    latitude = models.CharField(max_length=255,blank=True,null=True)
    longitude = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

class AreaServed(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    url = models.URLField(blank=True,null=True)

class ContactPoint(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255,blank=True,null=True)
    contactType = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)

class Employee(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    url = models.URLField()

class Image(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255,blank=True,null=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    url = models.ImageField(upload_to='images/')
    creator = models.CharField(max_length=255,blank=True,null=True)
    contentLocation = models.CharField(max_length=255,blank=True,null=True)




   

                     












