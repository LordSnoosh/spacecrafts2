from django.db import models

# Create your models here.
class Craft(models.Model):
    # from API
    cargo_capacity = models.IntegerField()
    consumables = models.CharField(max_length=100)
    cost_in_credits = models.IntegerField()
    crew = models.IntegerField()
    length = models.IntegerField()
    manufacturer = models.CharField(max_length=500)
    max_atmosphering_speed = models.IntegerField()
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    passengers = models.IntegerField()
    hyperdrive_rating = models.FloatField()
    url = models.CharField(max_length=100)
    # may or may not exist
    vehicle_class = models.CharField(max_length=100)
    starship_class = models.CharField(max_length=100)
    MGLT = models.CharField(max_length=100)
    # own stuff
    sell_price = models.IntegerField()
    BUCKET = 'Bucket'
    FAIR = 'Fair'
    GOOD = 'Good'
    EXCELLENT = 'Excellent'
    LIKE_NEW = 'Like New'
    CONDITION = (
        (BUCKET, 'Bucket'),
        (FAIR, 'Fair'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),
        (LIKE_NEW, 'Like New'),
    )
    condition = models.CharField(max_length=100, choices = CONDITION, default = GOOD)
    description = models.TextField(max_length=1000)
    mileage = models.IntegerField()
    date_created = models.DateTimeField(editable=False)
    
    def __str__(self): 
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        return super(User, self).save(*args, **kwargs)