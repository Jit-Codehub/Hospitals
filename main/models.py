from django.db import models

STATUS_CHOICE = (
    ("sunday", "Sunday"),
    ("monday", "Monday"),
    ("tuesday", "Tuesday"),
    ("wednesday", "Wednesday"),
    ("thursday", "Thursday"),
    ("friday", "Friday"),
    ("saturday", "Saturday"),
)

STATUS_PATIENT = (
    ("yes", "YES"),
    ("no", "NO"),
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
    map_id = models.URLField()
    additional_Type = models.URLField()
    medical_Specialty = models.CharField(max_length=255,null=True)
    curreny_Accepted = models.ManyToManyField(Currency)
    payment_Accepted = models.CharField(max_length=255,null=True)
    hasMap = models.CharField(max_length=1000,null=True)
    logo = models.URLField()
    telephone = models.CharField(max_length=255,null=True)
    isAcceptingNewPatients = models.CharField(max_length=255, choices=STATUS_PATIENT)
    knows_language = models.ManyToManyField(KnowsLanguage)
    url = models.URLField()
    name = models.CharField(max_length=255)
    AlternateName = models.CharField(max_length=255)
    description = models.TextField()
    disambiguatingDescription = models.TextField()
    foundingDate = models.CharField(max_length=255)
    SameAs = models.TextField()
    pub_type = models.CharField(max_length=255)
    publisher_id = models.URLField()
    pub_name = models.CharField(max_length=100)
    website_id = models.CharField(max_length=100)
    pub_url = models.URLField()




# class Website(models.Model):
#     type = models.CharField(max_length=255)
#     publisher_id = models.URLField()
#     name = models.CharField(max_length=100)
#     website_id = models.CharField(max_length=100)
#     url = models.URLField()

# class Haspart(models.Model):
#     website = models.ForeignKey(Website, on_delete=models.CASCADE)
#     h_type = models.CharField(max_length=255,null=True)
#     haspart_id = models.URLField()





    


class Haspart(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    h_type = models.CharField(max_length=255,null=True)
    haspart_id = models.URLField()


    


class AvailableService(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sameAs = models.URLField()
    description = models.TextField()
    url = models.URLField()


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
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    description = models.TextField()

class AreaServed(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    area_id = models.URLField()

class ContactPoint(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    contactType = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)

class Employee(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    emp_id = models.URLField()

class Image(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    url = models.URLField()
    creator = models.CharField(max_length=255)
    contentLocation = models.CharField(max_length=255)




   

                     













