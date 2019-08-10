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

    def hasPrev(self):
        first_entry = self.set.entry_set.first()
        if self == first_entry:
            return False
        return True

    def getPrev(self):
        return self.set.entry_set.filter(id__lt=self.id).last()

    def hasNext(self):
        last_entry = self.set.entry_set.last()
        if self == last_entry:
            return False
        return True

    def getNext(self):
        return self.set.entry_set.filter(id__gt=self.id).first()


   