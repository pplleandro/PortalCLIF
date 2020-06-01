from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import User, Group, Permission

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        ('Nome do Usuário', {'fields': ('username',)}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'groups',),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'getGroup', 'is_staff',)
    list_display_links = ('username', 'email', 'first_name', 'last_name', 'getGroup',)
    filter_horizontal = ['groups']

    def getGroup(self, obj):
        return ' | '.join([p.name for p in obj.groups.all()])

    getGroup.short_description = 'Grupos'


@admin.register(Group)
class GroupAdmin(GroupAdmin):
    list_display = ('name', 'getPerm')
    filter_vertical = ['permissions']

    def getPerm(self, obj):
        return ' | '.join([p.name for p in obj.permissions.all()])

    getPerm.short_description = 'Permissões'


class PermAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'name',)


#admin.site.register(Permission, PermAdmin)