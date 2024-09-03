from django.contrib import admin
from accounts.models import CustomUser
from .models import *  # Importa los modelos que quieras gestionar
from messaging.models import Message
from profiles.models import Profile

##class YourModelAdmin(admin.ModelAdmin):
  ##  list_display = ('field1', 'field2', 'field3')  # Campos que quieras mostrar en la vista del admin
    ##search_fields = ('field1', 'field2')  # Campos por los que quieras habilitar la búsqueda

##admin.site.register(YourModelAdmin)
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Message)
