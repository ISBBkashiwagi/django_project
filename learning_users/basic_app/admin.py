from django.contrib import admin
from basic_app.models import UserProfileInfo, MicroPost, IsbbEmployee

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(MicroPost)
admin.site.register(IsbbEmployee)