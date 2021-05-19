from django.contrib import admin
from teacher_app  import models

admin.site.register(models.UserProfile)
# admin.site.register(models.ProfileFeedItem)
admin.site.register(models.StudentItem)
admin.site.register(models.TeacherItem)
admin.site.register(models.StaffItem)
# Register your models here.
