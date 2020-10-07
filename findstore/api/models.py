from django.utils import timezone
from django.db import models


class Store(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    tel = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    main_mn = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    menu = models.CharField(max_length=200, null=True)
    opng_tm = models.CharField(max_length=200, null=True)
    rating = models.FloatField(max_length=200, null=True)
    rvw_cnt = models.FloatField(null=True)
    tags = models.CharField(max_length=200, null=True)
    img = models.CharField(max_length=200, null=True)

    @property
    def category_list(self):
        return self.category.split("/") if self.category else []

    @property
    def menu_list(self):
        return self.menu.split("//") if self.menu else []


class EnterStore(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    tel = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    main_mn = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    menu = models.CharField(max_length=200, null=True)
    opng_tm = models.CharField(max_length=200, null=True)
    rating = models.CharField(max_length=200, null=True)
    rvw_cnt = models.CharField(max_length=200, null=True)
    tags = models.CharField(max_length=200, null=True)
    img = models.CharField(max_length=200, null=True)
    
    @property
    def category_list(self):
        return self.category.split("/") if self.category else []

    @property
    def menu_list(self):
        return self.menu.split("//") if self.menu else []


class Reviews(models.Model):
    res_id = models.IntegerField()
    res_name = models.CharField(max_length=200, null=True)
    user_name = models.CharField(max_length=200, null=True)
    rating = models.IntegerField(null=True)
    review = models.CharField(max_length=200, null=True)
    sex = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    ppl = models.IntegerField(null=True)
    

class TestReviews(models.Model):
    res_id = models.IntegerField()
    res_name = models.CharField(max_length=200, null=True)
    user_name = models.CharField(max_length=200, null=True)
    rating = models.IntegerField(null=True)
    review = models.CharField(max_length=200, null=True)
    sex = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    ppl = models.IntegerField(null=True)


class Recommand(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=200)
    res_id = models.CharField(max_length=200, null=True)
    rating = models.FloatField(null=True)
    address = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    img = models.CharField(max_length=200, null=True)
    tags = models.CharField(max_length=200, null=True)


class CardData(models.Model):
    avg_age = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=200, null=True)
    ppl = models.CharField(max_length=200, null=True)
    time = models.CharField(max_length=200, null=True)
    dong = models.CharField(max_length=200, null=True)
    cnt = models.IntegerField(null=True)
