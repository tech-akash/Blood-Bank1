from django.contrib import admin
from .models import Accept,Donate,Customer
# Register your models here.

admin.site.register(Accept)
admin.site.register(Donate)
admin.site.register(Customer)