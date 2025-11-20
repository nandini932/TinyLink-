from django.db import models


class Link(models.Model):
    code = models.CharField(max_length=8, unique=True)
    target_url = models.URLField()
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_clicked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.code} -> {self.target_url}"