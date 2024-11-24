from rest_framework import serializers
from .models import Book
from datetime import datetime, timezone

class BookSerializer(serializers.ModelSerializer):
    days_since_publish = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['title','author','publish_date', 'days_since_publish']

    def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError("title must be 5 char long")
        return data
    
    def get_days_since_publish(self, obj):
        """
        since the publish_date field is a datetime.date field and the current time
        is being returned as a datetime.datetime field, there is need to convert
        the publish_date field result into a datetime.datetime result.
        here is how to do so:
        publish_datetime = datetime.combine(obj.publish_date, datetime.min.time(), tzinfo=timezone.utc)
        """
        publish_datetime = datetime.combine(obj.publish_date, datetime.min.time(), tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - publish_datetime).days


