from django.db import models

# Create your models here.
# job posting table 
#  include attribute like title, description , company detail , salary  


class Job(models.Model):
    # id-- starts at 1 and auto increment as user adds
    title = models.CharField(max_length=200)
    description = models.TextField( )
    company_detail = models.TextField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

#  makemigrations
#  instruction how the database table has changed  


 
#  migrate

# apply the change to the database table




# CRUD  OPERATIONS
# CREATE  :: CRETAING  new job board
# REMOVE :: remove items from job board
# UPDATE :: update the board
# DELETE :: delete items from



# models manager -> objects

# Job.objects.all() -> get all the objects from the database 
# Job.objects.get(id=1) -> get the objects from the database whose id is 1
# Job.objects.filter(company="abc tech") -> get the objects from the database whose id is 1
# 



# SHELL