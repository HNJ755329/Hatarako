from django.db import models
import uuid
from colorfield.fields import ColorField

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contents = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    industory = models.CharField(max_length=30)
    career = models.CharField(max_length=30)
    age = models.CharField(max_length=20)
    color = models.CharField(max_length=7)
    #color = ColorField(default='#FF0000')
    #color = models.ForeignKey('Color', on_delete=models.PROTECT)

    def __str__(self):
        return self.contents + "■" + self.industory + "／" + self.career + "・" + self.age + " colorindex:" + str(self.color)
    
    class Meta:
        verbose_name_plural = "はたらくことば投稿"



class Color(models.Model):
    web = models.CharField(max_length = 7)

    def __str__(self):
        return self.web

    class Meta:
        verbose_name_plural = "カラー設定"
