from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class About(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    content = CKEditor5Field(config_name='default')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/axror/', blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']

