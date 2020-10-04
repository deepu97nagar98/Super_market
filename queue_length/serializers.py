from rest_framework import serializers
from .models import Queue,QueueHistory

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model= Queue
        fields=('queue_id','queue_size', 'last_update')


class QueueHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model= QueueHistory
        fields='__all__'

        
