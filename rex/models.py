from django.db import models

# Create your models here.
class User(models.Model):
  def __str__(self):
    return self.question_text
  name = models.CharField(max_length=50)
  enrolment_number = models.IntegerField()
  email = models.EmailField()
  contact_number = models.IntegerField()

class Room(models.Model):
  def __str__(self):
    return self.question_text
  user = models.ForeignKey(User)
  room_number = models.CharField(max_length=4)
  description = models.TextField()
  preference = models.TextField()
  pub_date = models.DateTimeField('date published')
