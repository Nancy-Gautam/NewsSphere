from django.contrib import admin
from.models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','message')
admin.site.register(contactus,contactusAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','headlines','slider_Dec', 'slider_picture')
admin.site.register(slider,sliderAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name','category_picture')
admin.site.register(category,categoryAdmin)

class cityAdmin(admin.ModelAdmin):
    list_display = ('id','city_name','city_picture')
admin.site.register(city,cityAdmin)

class mynewsAdmin(admin.ModelAdmin):
    list_display = ('id','news_category','news_city')
admin.site.register(mynews,mynewsAdmin)

class vnewsAdmin(admin.ModelAdmin):
    list_display = ('id','vcategory','city','headlines','news','vlink','newsdate')

admin.site.register(vnews,)

class jobsAdmin(admin.ModelAdmin):
    list_display = ('id','job_title','job_link','job_picture')

admin.site.register(jobs,jobsAdmin)

