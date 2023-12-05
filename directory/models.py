from django.db import models
from utils.models import BaseModel

# Create your models here.


class Direction(BaseModel):
    title = models.CharField(max_length=255)
    is_new = models.BooleanField(default=False)


class SiteType(BaseModel):
    title = models.CharField(max_length=255)


class Site(BaseModel):
    title = models.CharField(max_length=255)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    url = models.URLField()
    about = models.TextField()
    types = models.ManyToManyField(SiteType)


class SiteLog(BaseModel):
    site = models.ForeignKey(
        Site, on_delete=models.CASCADE, related_name='logs')
    visitor_count = models.IntegerField(default=0)

    @classmethod
    def is_avaliable(cls, site, day):
        if cls.objects.filter(site=site, created_at__date=day).exists():
            return True
        return False

    def update_visitor_count(self):
        self.visitor_count += 1
        self.save()
