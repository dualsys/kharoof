from django.db import models
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
# Create your models here.
