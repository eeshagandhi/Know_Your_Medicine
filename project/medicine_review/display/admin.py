from django.contrib import admin
from .models import  medicine_data,post,Category,comment
# Register your models here.
admin.site.register(medicine_data)
admin.site.register(post)
admin.site.register(Category)
admin.site.register(comment)
