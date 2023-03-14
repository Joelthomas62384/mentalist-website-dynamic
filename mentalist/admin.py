from django.contrib import admin

from . models import thumbnail,UserPermissions,contents

admin.site.register(thumbnail)
admin.site.register(UserPermissions)
admin.site.register(contents)