from django.db import models
from .utils import get_link_data

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    img = models.URLField(null=True, blank=True)
    current_price = models.IntegerField(blank=True)
    old_price = models.IntegerField(default=0)
    price_difference = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ['-created']

    
    def convert_to_int(self, price_str):
        # Remove the thousand separators
        price_str = price_str.replace('.', '')
        return int(price_str)

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                name, price, img = get_link_data(self.url)
                self.name = name 
                self.current_price = self.convert_to_int(price)
                self.img = img 
            except Exception as e:
                # Handle potential errors in data fetching
                print(f"Error fetching data for link {self.url}: {e}")
        super().save(*args, **kwargs)
