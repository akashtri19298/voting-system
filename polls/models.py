from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    candidate_name=models.CharField(max_length=30)
    candidate_info=models.CharField(max_length=300)
    vote_count=models.IntegerField(default=0)
    profile_image = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.candidate_name
        
class Voter(models.Model):
    #candidate_name=models.CharField(max_length=30,default="NULL")
    #status=models.BooleanField(default=0)
    #voter_user=models.OneToOneField(User,on_delete=models.CASCADE)
    voter_name=models.CharField(max_length=30)
    voter_roll=models.CharField(max_length=10)
    voter_username=models.CharField(max_length=20)
    voter_email=models.CharField(max_length=50)
    voter_password=models.CharField(max_length=15)
    def __str__(self):
        return self.voter_name
    
class VoterDetails(models.Model):
    class Meta:
        verbose_name = 'Voter Details'
        verbose_name_plural = 'Voter Details'
        
    voter_user=models.OneToOneField(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=0)
    voter_roll=models.CharField(max_length=10,null=True)
    candidate_voted=models.ForeignKey(Candidate,on_delete=models.SET_NULL, null = True,blank=True )
    def __str__(self):
        return self.voter_user.username
    

    