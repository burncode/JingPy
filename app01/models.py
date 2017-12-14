from django.db import models


class Role(models.Model):
    name = models.CharField(verbose_name='角色名称', max_length=32)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    name = models.CharField(verbose_name='用户名称', max_length=32)

    def __str__(self):
        return self.name


class UserType(models.Model):
    title = models.CharField(verbose_name='类型名称', max_length=32)

    def __str__(self):
        return self.title
