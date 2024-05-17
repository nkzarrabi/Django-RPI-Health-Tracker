from django.db import models

# Create your models here. inventory/models.py
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    type = models.CharField(max_length=255)  # Showroom, Shipment, Client Location

    def __str__(self):
        return self.name
    
# inventory/models.py

from django.db import models

class Rug(models.Model):
    STYLE_CHOICES = [
        ('Oushak', 'Oushak'),
        ('Modern', 'Modern'),
        ('Afshar', 'Afshar'),
        # Add all other styles here
    ]

    TEXTURE_CHOICES = [
        ('Flatweave', 'Flatweave'),
        ('High-low', 'High-low'),
        ('Hooked', 'Hooked'),
        ('Pile', 'Pile'),
    ]

    CONDITION_CHOICES = [
        ('Antique', 'Antique'),
        ('Antique Reproduction', 'Antique Reproduction'),
        ('New', 'New'),
    ]

    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50, default='Unknown Size')
    age = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    country_of_origin = models.CharField(max_length=100, default='Unknown')
    texture = models.CharField(max_length=50, choices=TEXTURE_CHOICES)
    style = models.CharField(max_length=100, choices=STYLE_CHOICES)
    color = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    rug = models.ForeignKey(Rug, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rug_photos/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Photo for {self.rug.name}"


'''
class Rug(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    length = models.FloatField()
    width = models.FloatField()
    dominant_color = models.CharField(max_length=255)
    secondary_color = models.CharField(max_length=255)
    pattern = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    stock_number = models.CharField(max_length=255, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # Available, Sold, Reserved
    age = models.CharField(max_length=50)  # Antique, Antique Reproduction, New
    texture = models.CharField(max_length=50)  # Flatweave, High-Low, Hooked, Pile
    type = models.CharField(max_length=255)  # e.g., Oushak, Modern, Afshar

    def __str__(self):
        return self.name
'''
class Client(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.TextField()

    def __str__(self):
        return self.name

class Sale(models.Model):
    rug = models.ForeignKey(Rug, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_of_sale = models.DateField()
    sale_price = models.FloatField()

    def __str__(self):
        return f"Sale of {self.rug.name} to {self.client.name}"

class InventoryMovement(models.Model):
    rug = models.ForeignKey(Rug, on_delete=models.CASCADE)
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='from_location')
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='to_location')
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"Movement of {self.rug.name}"

class MaintenanceRecord(models.Model):
    rug = models.ForeignKey(Rug, on_delete=models.CASCADE)
    date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"Maintenance of {self.rug.name} on {self.date}"

class Report(models.Model):
    REPORT_TYPES = [
        ('Inventory', 'Inventory'),
        ('Sales', 'Sales'),
        ('Maintenance', 'Maintenance'),
    ]
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    generated_by = models.CharField(max_length=255)
    date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return f"{self.report_type} Report on {self.date}"