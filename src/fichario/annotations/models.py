import time, hashlib
from django.db import models
from colorfield.fields import ColorField
from fichario.synchronization.models import SyncedModel

COLOR_PALETTE = [
    ('#FFFFFF00', _('No color')),
    ('#FFFFFFFF', _('White')),
    ('#000000FF', _('Black')),
    ('#FF0000FF', _('Red')),
    ('#800000FF', _('Maroon')),
    ('#8b4513FF', _('Brown')),
    ('#918151FF', _('Tan')),
    ('#f94d00FF', _('Orange')),
    ('#ffe5b4FF', _('Peach')),
    ('#fcc200FF', _('Gold')),
    ('#ffff00FF', _('Yellow')),
    ('#00ff00FF', _('Lime')),
    ('#556b2fFF', _('Olive')),
    ('#008000FF', _('Green')),
    ('#7fffd4FF', _('Aquamarine')),
    ('#367588FF', _('Teal Blue')),
    ('#00ffffFF', _('Cyan')),
    ('#87ceebFF', _('Sky Blue')),
    ('#0000ffFF', _('Blue')),
    ('#000070FF', _('Navy Blue')),
    ('#800080FF', _('Purple')),
    ('#8a2be2FF', _('Violet')),
    ('#da70d6FF', _('Orchid')),
    ('#dcd0ffFF', _('Lavender')),
]

class ColorfulModel(models.Model):
    """Model with a color field"""
    color = ColorField(format='hexa', choices=COLOR_PALETTE, default=COLOR_PALETTE[0][0])
    
    class Meta:
        abstract = True

class Tag(models.Model):
    name = models.CharField(max_length=300)
    
    def natural_key(self):
        return self.name

class TaggableModel(models.Model):
    tags = models.ManyToManyField(to=Tag, blank=True)
    
    class Meta:
        abstract = True

class Project(SyncedModel, ColorfulModel, TaggableModel):
    name = models.CharField(max_length=300)

class Text(SyncedModel, ColorfulModel, TaggableModel):
    author = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    edition = models.CharField(max_length=300, blank=True)

class Annotation(SyncedModel, ColorfulModel, TaggableModel):
    text = models.ForeignKey(to=Text, on_delete=models.CASCADE)
    place = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    project = models.ForeignKey(to=Project, on_delete=models.PROTECT, blank=True, null=True)
