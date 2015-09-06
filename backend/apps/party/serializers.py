from rest_framework import serializers
import models


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Party
        fields = ('id', 'name')

