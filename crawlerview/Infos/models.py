from django.db import models

# 生成表名为：City_anqing   app名+类名 配置了class Meta:就可以按照自己的定义配置表名
# Create your models here.
class Infos(models.Model):
    city = models.CharField(max_length=10)
    title = models.CharField(unique=True, max_length=250)
    time = models.CharField(max_length=300)
    link = models.CharField(max_length=300)
    # CharField（相当于varchar）、DateField（相当于datetime）

    class Meta:
        managed = True
        db_table = 'infos'
