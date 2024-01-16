from rest_framework import serializers
from kasaparty.models.mpago import Mpago

class MpagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpago
        fields = "__all__"