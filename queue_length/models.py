from django.db import models

# Create your models here.

class Queue(models.Model):
    queue_id=models.IntegerField(primary_key=True)
    queue_size=models.IntegerField(null=False)
    last_update=models.DateTimeField(auto_now=True, null=False)


class QueueHistory(models.Model):
    queue_hist_id=models.AutoField(primary_key=True)
    queue_id=models.IntegerField(null=False)
    queue_size=models.IntegerField(null=False)
    last_update_at=models.DateTimeField(auto_now=True,null=False)
    