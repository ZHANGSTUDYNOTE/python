from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    def __str__(self):
        return self.pk


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    hBook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)  # 设置外键的时候都要设置的一个参数，指定多对一的时候多方持有一方的外键。

    def __str__(self):
        return "%d" % self.pk
