from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UploadedFile)
admin.site.register(SubPage)
admin.site.register(IndexEditor)
admin.site.register(SideLinkForIndex)
admin.site.register(DropdownTag)
admin.site.register(DropdownURL)

#
# class adminCategories(admin.ModelAdmin):
#     list_display = ['name']
#
#
# class adminParentCheck(admin.ModelAdmin):
#     list_display = ['sub']
#
#
# class adminMainPage(admin.ModelAdmin):
#     category_fieldsets = [
#         (None,  {'category_fields': ['name']})
#     ]
#
#     parentcheck_fieldsets = [
#         (None,  {'parentcheck_fields': ['sub']})
#     ]
#     category_list_display = ['name']
#     parentcheck_list_display = ['sub']
#
#
# admin.site.register(MainPage, adminMainPage)
# admin.site.register(Categories, adminCategories)
# admin.site.register(ParentCheck, adminParentCheck)
# admin.site.register(SubPage)

