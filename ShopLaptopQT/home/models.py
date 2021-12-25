from django.db import models
statusChoice = ((1,'Hien Thi'),(0,'An'))
class Category(models.Model):
    cat_id = models.AutoField(primary_key='true')
    cat_name = models.CharField(max_length=50, null=False)
    cat_image = models.ImageField(max_length=255)
    status = models.SmallIntegerField(choices=statusChoice)
    date_create = models.DateField()
    class Meta:
        db_table = "tbl_Category"
class Product(models.Model):
    listCategory = Category.objects.all()
    result = []
    for item in listCategory:
        result.append(
            (item.cat_id,item.cai_name)
        )
    pro_id = models.AutoField(primary_key='true')
    pro_name = models.CharField(max_length=50, null=False)
    cat_id = models.IntegerField(null=False, choices=result)
    pro_image = models.ImageField(max_length=255, null= False)
    pro_price = models.FloatField()
    description = models.TextField()
    status = models.SmallIntegerField(choices= statusChoice)
    date_create = models.DateField()
    class Meta:
        db_table = 'tbl_Product'
            