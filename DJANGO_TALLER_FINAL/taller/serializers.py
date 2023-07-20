from taller.models import Inscrito
from rest_framework import serializers

class InscritoSerial(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = '__all__'