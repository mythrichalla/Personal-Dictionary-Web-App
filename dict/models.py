from django.db import models

# Create your models here.
class Set(models.Model):
    title = models.CharField(max_length = 64, null = False, blank = False)
    description = models.CharField(max_length = 255, null = False, blank = True)

    def __str__(self):
        return self.title 
          

class Entry(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    term = models.TextField()
    definition = models.TextField()

    def __str__(self):
        return self.term