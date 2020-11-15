from django.db import models
from user.models import Profile 
from django.utils import timezone
# Create your models here.
class Quote(models.Model):
    userp=models.ForeignKey(Profile,on_delete=models.CASCADE)
    qoute=models.CharField(max_length=700)
    qoute_date=models.DateTimeField(default=timezone.now,auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return (f'user:{self.userp} qoute:{self.qoute}')

    class Meta:
        ordering = ('-qoute_date', )