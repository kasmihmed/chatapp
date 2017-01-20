from rest_framework import serializers
#from books.helpers import SlugifyUniquely
from chat.models import Message
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault


class Messageserializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    receiver_email = serializers.EmailField(required=False)
    receiver = serializers.SlugRelatedField(many=False,read_only=True, slug_field='email')
    body = serializers.CharField(required=True,max_length=500)
    seen = serializers.BooleanField(default=False,required=False)
    created_on = serializers.DateTimeField(required=False)
    updated_on = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Message` instance, given the validated data.
        """
        #validated_data["author"] = self.context['request'].user
        try:
            receiver = User.objects.get(email=validated_data["receiver_email"])
            validated_data["receiver"] = receiver
            print validated_data
            del validated_data["receiver_email"]
            return Message.objects.create(**validated_data)
        except User.DoesNotExist:
            return {'error':'receiver not found'}


