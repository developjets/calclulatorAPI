from rest_framework import serializers
from .models import RequestLogs

class CalculatorSerilizer(serializers.ModelSerializer):
    firstValue = serializers.IntegerField(required = True)
    secondValue = serializers.IntegerField(required = True)
    operationName = serializers.CharField(max_length=50, required = True)
    appName = serializers.CharField(max_length=50, required = True)

    class Meta:
        model = RequestLogs
        fields = ('__all__')