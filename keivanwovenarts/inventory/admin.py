# inventory/admin.py

from django.contrib import admin
from .models import Supplier, Location, Rug, Client, Sale, InventoryMovement, MaintenanceRecord, Report

admin.site.register(Supplier)
admin.site.register(Location)
admin.site.register(Rug)
admin.site.register(Client)
admin.site.register(Sale)
admin.site.register(InventoryMovement)
admin.site.register(MaintenanceRecord)
admin.site.register(Report)
# inventory/admin.py



#admin.site.register(Rug)
