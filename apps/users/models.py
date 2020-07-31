from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    扩展用户，需要在settings设置model
    """
    GENDER_CHOICES = (
        ('male', '男'), ('female', '女')
    )
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name='姓名', help_text='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月', help_text='出生年月')
    mobile = models.CharField(max_length=11, verbose_name='电话', help_text='电话')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male',
                              verbose_name='性别', help_text='性别')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        # 要判断name是否有值，如果没有，则返回username，否则使用creatsuperuser创建用户访问与用户关联的模型会报错，
        if self.name:
            return self.name
        else:
            return self.username


class VerifyCode(models.Model):
    """
    短信验证码，可以保存在redis等中
    """
    code = models.CharField(max_length=20, verbose_name='验证码', help_text='验证码')
    mobile = models.CharField(max_length=11, verbose_name='电话', help_text='电话')
    add_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
