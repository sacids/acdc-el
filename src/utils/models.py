from django.db import models
from authtools.models import User

# Create your models here.
class BaseModel(models.Model):
    created_on      = models.DateTimeField(auto_now_add=True, editable=False)
    created_by      = models.ForeignKey(User, related_name='course_created_by', on_delete=models.PROTECT)

class Meta:
    abstract=True # Set this model as Abstract