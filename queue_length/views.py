from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Queue,QueueHistory
from .serializers import QueueSerializer,QueueHistorySerializer
import datetime
from django.utils import timezone
from django.db.models import Max
class QueueController(APIView):

	def get(self, request):
		Queobj = Queue.objects.all()
		serializer = QueueSerializer(Queobj, many=True)
		return Response(serializer.data)

	def post(self,request):
		serializeobj=QueueSerializer(data=request.data)
		if serializeobj.is_valid():
			serializeobj.save()
			return Response(serializeobj.data,status=status.HTTP_201_CREATED)
		return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)	


class Queue_update(APIView):
 	def get_object(self, pk):
 		try:
 			return Queue.objects.get(queue_id=pk)
 		except Queue.DoesNotExist:
 			return 0

 	def get(self, request, pk, format=None):
 		queobj = self.get_object(pk)
 		serializer = QueueSerializer(queobj.data)
 		return Response(serializer.data,status=status.HTTP_200_OK)
 	
 	def put(self,request,pk): 		
 		queobj = self.get_object(pk)  			
 		if queobj == 0:
 		 	return Response(data='queue_id is not found')
 		serializer=QueueSerializer(queobj,data=request.data) 		
 		prev_time=datetime.datetime.now()-datetime.timedelta(minutes=5)
 		que1= QueueHistory.objects.filter(queue_id=pk,last_update_at__gte=prev_time)
 		que1=que1.aggregate(Max('queue_size'))['queue_size__max']
 		if serializer.is_valid() and (que1 is None or(que1-50 >= (request.data['queue_size']) )):
 			serializer.save() 
 			hit = QueueHistory(queue_id  = pk , queue_size = request.data['queue_size'])
 			hit.save()
 			return Response(serializer.data)
 		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)	

class queue_history(APIView):
	def get(self,request,pk):
		queue1= QueueHistory.objects.filter(queue_id=pk)
		serializer = QueueHistorySerializer(queue1, many=True)
		return Response(serializer.data)

