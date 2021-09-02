from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    building_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    floor = models.IntegerField(default=0)
    bedroom = models.IntegerField(default=0)
    bathroom = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    parking_available = models.CharField(max_length=10)
    two_wheeler = models.IntegerField(default=0)
    four_wheeler = models.IntegerField(default=0)
    yearly_maintenance = models.IntegerField(default=0)
    furnishing = models.CharField(max_length=20)
    gym = models.CharField(max_length=3)
    swimming_pool = models.CharField(max_length=3)
    playground = models.CharField(max_length=3)
    power_backup = models.CharField(max_length=3)
    club_house = models.CharField(max_length=3)
    locality = models.CharField(max_length=50)
    estate = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    date_added = models.DateTimeField('property_added')
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.type
