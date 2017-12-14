from django.shortcuts import HttpResponse
from django.utils.safestring import mark_safe
from stark.service import router
from app01 import models


class UserInfoConfig(router.StarkConfig):
    def checkbox(self, obj=None, is_header=False):
        if is_header:
            return '选择'
        return mark_safe('<input type="checkbox" name="pk" value="%s" />' % (obj.id,))

    def edit(self, obj=None, is_header=False):
        if is_header:
            return '编辑'
        return mark_safe('<a href="/edit/%s">编辑</a>' % (obj.id,))

    list_display = [checkbox, 'id', 'name', edit]


router.site.register(models.UserInfo, UserInfoConfig)

class RoleConfig(router.StarkConfig):
    list_display = ['name', ]


router.site.register(models.Role, RoleConfig)  # StarkConfig(Role)


class UserTypeConfig(router.StarkConfig):
    list_display = ['id', 'title']


router.site.register(models.UserType, UserTypeConfig)  # StarkConfig(Role)
