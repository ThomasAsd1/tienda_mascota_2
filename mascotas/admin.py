from django.contrib import admin
from .models import Post,mascota,cliente,compra,producto

admin.site.register(Post)
admin.site.register(mascota)
admin.site.register(cliente)
admin.site.register(compra)
admin.site.register(producto)