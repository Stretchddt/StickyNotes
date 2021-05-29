from django.db import models

# Create your models here.
class StickyNote(models.Model):
    title = models.CharField(max_length=300)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title