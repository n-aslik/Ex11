from django.contrib import admin
from .models import worker,pol,structure,User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User,UserAdmin)
admin.site.register(pol)
admin.site.register(structure)
admin.site.register(worker)
