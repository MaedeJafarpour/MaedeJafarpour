from django.db import models


class IPAddress(models.Model):
    ip = models.CharField(max_length=45, unique=True)  
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip} - {self.country}"

