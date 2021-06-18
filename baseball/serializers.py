from django.db import models
from rest_framework import serializers

from .models import Batters, Pitchers, PlayerInfo


class BatterDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batters
        exclude = ["player"]


class PitcherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pitchers
        exclude = ["player"]


class PlayerDetailSerializer(serializers.ModelSerializer):
    batting_stats = BatterDetailSerializer(many=True, read_only=True)
    pitching_stats = PitcherDetailSerializer(many=True, read_only=True)

    class Meta:
        model = PlayerInfo
        fields = [
            "name",
            "default_batting",
            "bat_career",
            "bat_peak",
            "bat_avg",
            "career_pas",
            "peak_pas",
            "bat_rate_career",
            "bat_rate_peak",
            "bat_rate_avg",
            "pit_career",
            "pit_peak",
            "pit_avg",
            "pit_rate_career",
            "pit_rate_peak",
            "pit_rate_avg",
            "career_ip",
            "peak_ip",
            "batting_stats",
            "pitching_stats",
        ]


class PlayerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInfo
        exclude = ["fplayerid"]


class BattingLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInfo
        fields = [
            "id",
            "name",
            "first_year",
            "last_year",
            "bat_career",
            "bat_peak",
            "bat_avg",
            "career_pas",
            "peak_pas",
            "bat_rate_career",
            "bat_rate_peak",
            "bat_rate_avg",
        ]


class PitchingLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInfo
        fields = [
            "id",
            "name",
            "first_year",
            "last_year",
            "pit_career",
            "pit_peak",
            "pit_avg",
            "career_ip",
            "peak_ip",
            "pit_rate_career",
            "pit_rate_peak",
            "pit_rate_avg",
        ]
