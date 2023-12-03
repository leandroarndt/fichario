from django.db import models

def create_hash():
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return  hash.hexdigest()[:-10]

# Create your models here.
class SyncedModel(models.Model):
    """A model that can be synced through many devices."""
    hash = models.CharField(max_length=10, default=create_hash, unique=True, primary_key=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)
    device = models.CharField(max_length=100, editable=False)
    
    class Meta:
        abstract = True