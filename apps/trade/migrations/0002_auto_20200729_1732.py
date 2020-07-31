# Generated by Django 3.0.8 on 2020-07-29 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0001_initial'),
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, related_name='shopping_carts', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='user',
            field=models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, related_name='order_infos', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='goods',
            field=models.ForeignKey(blank=True, help_text='商品', null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(help_text='订单信息', on_delete=django.db.models.deletion.CASCADE, related_name='order_goods', to='trade.OrderInfo', verbose_name='订单信息'),
        ),
    ]
