from django.db import models
from django.forms import ModelForm


class Image(models.Model):
    type_choices = (('junos_vmx', 'Junos vMX <= 14.1'), ('junos_firefly', 'Junos Firefly'), ('junos', 'Junos Other'),
                    ('linux', 'Linux'), ('other', 'Other'), ('junos_vmx_p2', 'Junos vMX >= 14.2'))
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=32, choices=type_choices, default='junos_vmx')
    description = models.TextField()
    filePath = models.FileField(upload_to='user_images')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Images'
        verbose_name_plural = 'images'


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'type', 'filePath', 'description']
