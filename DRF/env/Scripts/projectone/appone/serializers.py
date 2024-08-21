from rest_framework import serializers
from .models import LeadModule

class LeadSerializer(serializers.ModelSerializer):

    class meta:

        model=LeadModule
        fields="__all__"