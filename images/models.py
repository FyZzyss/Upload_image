from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='image')

    def __str__(self):
        return self.docfile