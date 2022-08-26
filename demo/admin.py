from django.contrib import admin
from  .models import *

admin.site.register(User)
# admin.site.register(UserNdPassword)
admin.site.register(Question)
admin.site.register(Choice)
