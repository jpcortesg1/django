from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'document_type', 'document_number',
                  'name', 'last_name', 'hobbies', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at',)
