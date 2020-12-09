
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver
import statistics
from PIL import Image


class StudentUnion(models.Model):
    union_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    # union_photo = ImageField(blank=True, manual_crop="")
    union_photo = CloudinaryField('union_photo',blank=True)
    union_name = models.TextField(max_length=500)
    union_location = models.CharField(max_length=60, blank=True)
    union_members = models.IntegerField(default=0)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.union_name

    class Meta:
        ordering = ['create_at'] 

    def create_studentunion(self):
      '''
      Saves StudentUnion instance to db
      '''
      self.save()

    @classmethod
    def delete_studentunion(cls,union_id):
      '''
      Deletes StudentUnion based on its id
      '''
      cls.objects.filter(id=union_id).delete()
      

    @classmethod
    def get_all_studentunions(cls):
      '''
      Returns all StudentUnion objects from db
      '''
      unions=cls.objects.all()
      return unions 


    @classmethod
    def find_studentunion(cls,union_id):
      '''
      Returns StudentUnion based on its id
      '''
      union=cls.objects.get(id=union_id)
      return union


class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    studentunion = models.ForeignKey(StudentUnion, on_delete=models.CASCADE)
    bs_name = models.TextField(max_length=120)
    bs_description = models.TextField(blank=True)
    bs_photo = CloudinaryField('bs_photo',blank=True)
    # bs_photo = ImageField(blank=True, manual_crop="")
    bs_email = models.EmailField(max_length=254)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bs_name

    class Meta:
        ordering = ['create_at'] 

    def create_business(self):
      '''
      Saves Business instance to db
      '''
      self.save()

    def delete_business(self):
      '''
      Deletes Business instance from db
      '''
      self.delete()
      

    @classmethod
    def get_all_bs_by_union(cls,union_id):
      '''
      Returns all Businesses in the union objects from db
      '''
      bs=cls.objects.filter(studentunion_id=union_id)
      return bs 


    @classmethod
    def find_business(cls,bs_id):
      '''
      Returns Business based on its id
      '''
      bs=cls.objects.get(id=bs_id)
      return bs


    @classmethod
    def search_business(cls, name,union_id):
      '''
      Returns Business search based on its name and user student union
      '''
      return cls.objects.filter(bs_name__icontains=name , studentunion_id=union_id)




class Post(models.Model):
    """
    Post class to define Post Objects
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    studentunion = models.ForeignKey(StudentUnion, on_delete=models.CASCADE)
    post_title = models.CharField(max_length =150)
    post_text = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title


    class Meta:
        ordering = ['upload_date'] 



class EmergencyService(models.Model):
    stype = (
        ('Hospital', 'Hospital'),
        ('Security', 'Security'),
        ('Acc', 'Acc')
    )
    studentunion = models.ForeignKey(StudentUnion, on_delete=models.CASCADE)
    name = models.CharField(max_length =150)
    service_type = models.CharField(choices=stype,max_length=60)
    location = models.CharField(max_length=60, blank=True)
    contact = models.CharField(max_length=60,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


    class Meta:
        ordering = ['create_at'] 


        
      


   