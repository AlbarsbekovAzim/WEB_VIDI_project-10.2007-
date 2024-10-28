from django.db import models

# Create your models here.
class btns(models.Model):
     title = models.CharField('text in button', max_length=50)

     def __str__(self):
          return self.title
     
     class Meta:
          verbose_name = 'button content'
          verbose_name_plural = 'button content'

class imgs(models.Model):
     image = models.ImageField('image instead of credit card')

     def __img__(self, obj):
          return self.image
            # return format_html('<img src="{self.image}" class = "first-selection_image" />'.format(obj.image.url))
     
     class Meta:
          verbose_name = 'what image'
          verbose_name_plural = 'what image'
