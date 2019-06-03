from django.contrib import admin

from .models import Profile,Relationship,People,requests
# Register your models here.


admin.site.register(requests)
admin.site.register(People)
admin.site.register(Relationship)
admin.site.register(Profile)
