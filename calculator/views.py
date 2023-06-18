from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RequestLogs
from .serializers import CalculatorSerilizer

# Create your views here.

class CalculatorView(APIView):

    def get(self, *args, **kwargs):
        logs = RequestLogs.objects.all()
        serializers = CalculatorSerilizer(logs, many=True)
        return Response({'status':'success', "Logs":serializers.data}, status=200)
    
    def post(self, request, *args, **kwargs):
        serializers = CalculatorSerilizer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            a = serializers.validated_data['firstValue']
            b = serializers.validated_data['secondValue']
            operation = serializers.validated_data['operationName']
            if operation == "add":
                c = a + b
                return Response({"status":"success", "data":serializers.data, "result": c},status=status.HTTP_200_OK)
            if operation == "subtract":
                c = a - b
                return Response({"status":"success", "data":serializers.data, "result": c},status=status.HTTP_200_OK)
            if operation == "multiply":
                c = a * b
                return Response({"status":"success", "data":serializers.data, "result": c},status=status.HTTP_200_OK)
            if operation == "division":
                c = a / b
                return Response({"status":"success", "data":serializers.data, "result": c},status=status.HTTP_200_OK)
        else: 
            return Response({"status":"error", "data":serializers.data},status=status.HTTP_400_BAD_REQUEST)
