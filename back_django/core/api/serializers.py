from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Report, ReportResponse


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class ReportResponseSerializer(serializers.ModelSerializer):

    author = UserSerializer()

    class Meta:
        model = ReportResponse
        fields = ('message', 'author')


class ReportSerializer(serializers.ModelSerializer):

    author = UserSerializer()
    supervisors = UserSerializer(many=True)
    responses = ReportResponseSerializer(source='response_set', many=True)

    class Meta:
        model = Report
        depth = 1
        fields = ('id', 'message', 'author', 'supervisors', 'responses')
