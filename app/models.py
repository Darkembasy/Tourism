from django.db import models

# Create your models here.
class Content:
  name: str
  content1: str
  content2: str
  content3: str
  content4: str

class Traveler(models.Model):
  traveler_id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  phone_number = models.CharField(max_length=50)

class Accommodation(models.Model):
  accommodation_id = models.AutoField(primary_key=True)
  room_type = models.CharField(max_length=50)
  capacity = models.IntegerField()
  amenities = models.TextField()
  price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.amenities

class Attraction(models.Model):
  attraction_id = models.AutoField(primary_key=True)
  opening_hours = models.CharField(max_length=50)
  ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
  rating = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.address

class Destination(models.Model):
  destination_id = models.AutoField(primary_key=True)
  address = models.CharField(max_length=30)
  traveler_id = models.ForeignKey(Traveler, on_delete=models.CASCADE)
  accommodation_id = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
  attraction_id = models.ManyToManyField(Attraction)

  def __str__(self):
    return self.location

class Activity(models.Model):
  activity_id = models.AutoField(primary_key=True)
  type = models.CharField(max_length=50)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  duration = models.IntegerField()
  destination_id = models.ManyToManyField(Destination)

  def __str__(self):
    return self.description

class Review(models.Model):
  review_id = models.AutoField(primary_key=True)
  date_created = models.DateField(auto_now_add=True)
  text = models.TextField()
  activity = models.ManyToManyField(Activity)

  def __str__(self):
    return self.user


