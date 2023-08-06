from django.db import models

# Create your models here.

JOP_TYPE=(
    ('Full time','Full time'),
    
    ('Part time','Part time'),

)
class job(models.Model):
    title=models.CharField(max_length=120)
    #location
    jop_type=models.CharField(max_length=15,choices=JOP_TYPE,default="Full time")
    descraption=models.TextField(max_length=30,default=" ")
    puplished_at=models.DateTimeField(auto_now=True,auto_now_add=False)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    exprince=models.IntegerField(default=1)
    
    
    def __str__(self):
        return f'{self.title+"------------>"}{self.puplished_at}'
    
    
 

    
    
    