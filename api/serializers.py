from rest_framework import serializers
from .models import League, Team, Player

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'