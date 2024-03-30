from django.db import models

# Create your models here.

class States(models.Model):
    date = models.DateField()
    state = models.CharField(max_length=50)
    fips = models.IntegerField()
    cases = models.IntegerField()
    deaths = models.IntegerField()

    class META:
        constraints = [
            models.UniqueConstraint(fields=['date', 'state'], name='unique_state_date')
        ]

class Counties(models.Model):
    date = models.DateField()
    county = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    fips = models.IntegerField()
    cases = models.IntegerField()
    deaths = models.IntegerField()

    class META:
        constraints = [
            models.UniqueConstraint(fields=['date', 'county'], name='unique_county_date')
        ]  

class FaceMasks(models.Model):
    countyfp = models.IntegerField()
    never = models.FloatField()
    rarely = models.FloatField()
    sometimes = models.FloatField()
    frequently = models.FloatField()
    always = models.FloatField()
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['countyfp'], name='unique_countyfp')
        ]