from django.db import models


class Document(models.Model):
    docfile = models.ImageField(upload_to='image')

    def __str__(self):
        return str(self.docfile)