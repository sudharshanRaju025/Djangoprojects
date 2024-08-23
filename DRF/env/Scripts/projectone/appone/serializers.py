from rest_framework import serializers
from .models import LeadModule

class LeadSerializer(serializers.ModelSerializer):

    class Meta:

        model=LeadModule
        fields="__all__"