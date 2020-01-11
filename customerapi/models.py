from django.db import models

import uuid
class Products(models.Model):
    item_id = models.AutoField(primary_key=True, editable=False)
    item_title = models.TextField(max_length=255,null=True)
    item_description = models.TextField(null=True)
    months = models.CharField(max_length=255,null=True)
    size = models.CharField(max_length=255,null=True)
    origin = models.CharField(max_length=255,null=True)
    weight = models.CharField(max_length=255,null=True)
    price = models.CharField(max_length=255,null=True)
    item_image = models.TextField(max_length=255,null=True)
    class Meta:
        db_table = 'items'
        managed = False
    def __self__(self):
        return self.item_title
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True, editable=False)
    customer_id = models.BigIntegerField(null=False)
    contact_number = models.BigIntegerField(max_length=255, null=False)
    restaurant_id = models.BigIntegerField(max_length=255, default=0)
    menu_id = models.BigIntegerField(max_length=255, default=0)
    slaughterhouse_id = models.BigIntegerField(max_length=255, default=0)
    driver_id = models.BigIntegerField(max_length=255, default=0)
    delivery_address = models.TextField(null=True)
    delivery_date = models.CharField(max_length=255,null=True)
    delivery_latlng = models.TextField(null=True)
    total_amount = models.TextField(null=True)
    online_txt_number = models.TextField(null=True)
    payment_status = models.CharField(max_length=255, default=0)
    restaurant_accept_status = models.CharField(max_length=255, default=0)
    driver_accept_status = models.CharField(max_length=255, default=0)
    order_date = models.CharField(max_length=255, default=0)
    order_time = models.CharField(max_length=255, default=0)
    class Meta:
        db_table = 'orders'
        managed = False
    def __self__(self):
        return self.order_id

class OrderTimeLine(models.Model):
    order_timeline_id = models.AutoField(primary_key=True, editable=False)
    order_id = models.BigIntegerField(max_length=255, null=False)
    timeline_title = models.TextField(null=True)
    order_time =  models.CharField(max_length=255, default=0)
    order_date =  models.CharField(max_length=255, default=0)
    class Meta:
        db_table = 'order_timeline'
        managed = False
    def __self__(self):
        return self.timeline_title
        
class Customers(models.Model):
    ledger_id = models.AutoField(primary_key=True, editable=False)
    ledger_title = models.TextField(max_length=255,null=True)
    login_id = models.CharField(max_length=255,null=True)
    login_password = models.CharField(max_length=255,null=True)
    contact_number = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    fcm_token = models.TextField(max_length=255,null=True)
    class Meta:
        db_table = 'ledgers'
        managed = False
    def __self__(self):
        return self.ledger_title

# Create your models here.
