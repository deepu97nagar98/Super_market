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
 			raise Http404

 	def get(self, request, pk, format=None):
 		queobj = self.get_object(pk)
 		serializer = QueueSerializer(queobj)
 		return Response(serializer.data)

 	def put(self,request,pk):
 		# queue_id= request.data['queue_id']
 		queobj = self.get_object(pk)
 		# print(queobj)
 		if queobj==0:
 			return Response(data='queue_id is not found')
 		serializer=QueueSerializer(queobj,data=request.data)
 		# print(queobj.queue_size)
 		# print(serializer.data['queue_size'])
 		# print(request.data['queue_size'])
 		current_time=datetime.datetime.now()
 		prev_time=current_time-datetime.timedelta(minutes=5)
 		que1= QueueHistory.objects.filter(queue_id=pk)
 		que1=que1.filter(last_update_at__gte=prev_time)
 		que1=que1.aggregate(Max('queue_size'))['queue_size__max']
 		# print(que1)
 		# print(prev_time)
 		# print(current_time)
 		if que1 is None:
 			return Response("entry is not allowed")
 		if serializer.is_valid() and (que1-50 >= int(request.data['queue_size']) or que1 is None):
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
