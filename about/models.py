from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class About(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    content = CKEditor5Field(default_config_name='default')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']

