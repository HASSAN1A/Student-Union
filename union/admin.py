from django.contrib import admin
from .models import StudentUnion,Business,Post,EmergencyService
# Register your models here.
admin.site.register(StudentUnion)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(EmergencyService)
