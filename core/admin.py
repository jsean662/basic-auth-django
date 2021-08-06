from django.contrib import admin
from core.models import UserLoginHistory
from import_export.admin import ExportActionMixin
from import_export import resources


class UserLoginHistoryResource(resources.ModelResource):

    class Meta:
        model = UserLoginHistory
        fields = ['id', 'dateCreated', 'userId__username', 'ip']

class UserLoginHistoryAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = UserLoginHistoryResource
    search_fields = ('userId__username',)
    list_display = ['id', 'dateCreated', 'userId', 'ip']


admin.site.register(UserLoginHistory, UserLoginHistoryAdmin)
        