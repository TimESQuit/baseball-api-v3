from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination

from .models import PlayerInfo
from .serializers import (
    BattingLeaderSerializer,
    PitchingLeaderSerializer,
    PlayerDetailSerializer,
    PlayerInfoSerializer,
)


class PlayerDetail(generics.RetrieveAPIView):
    queryset = PlayerInfo.objects.all()
    serializer_class = PlayerDetailSerializer


class Leaderboards(generics.ListAPIView):
    def get_serializer_class(self):
        if self.kwargs.get("player_type") == "batting":
            return BattingLeaderSerializer
        else:
            return PitchingLeaderSerializer

    def get_queryset(self):

        when_player = self.kwargs.get("when_player")
        player_type = self.kwargs.get("player_type")

        if when_player not in ["career", "active"] or player_type not in [
            "batting",
            "pitching",
        ]:
            raise NotFound()

        career = when_player == "career"
        bat = player_type == "batting"

        queryset = PlayerInfo.objects.all()
        actives = PlayerInfo.objects.filter(last_year__in=[2019, 2020]).values_list(
            "id", flat=True
        )

        field_asc = self.request.query_params.get("asc")
        if field_asc == "true":
            field_asc = True
        else:
            field_asc = False

        order_by_field = self.request.query_params.get("orderby") or (
            "bat_career" if bat else "pit_career"
        )
        if not field_asc:
            order_by_field = "-" + order_by_field

        if bat:
            if career:
                return queryset.filter(bat_career__gte=20).order_by(
                    order_by_field, "id"
                )
            else:
                return (
                    queryset.filter(id__in=actives)
                    .filter(career_pas__gte=500)
                    .order_by(order_by_field, "id")
                )
        else:
            if career:
                return queryset.filter(pit_career__gte=20).order_by(
                    order_by_field, "id"
                )
            else:
                return (
                    queryset.filter(id__in=actives)
                    .filter(career_ip__gte=150)
                    .order_by(order_by_field, "id")
                )


class PlayerSearch(generics.ListAPIView):
    serializer_class = PlayerInfoSerializer

    def get_queryset(self):
        queryset = PlayerInfo.objects.all()

        query = self.request.query_params.get("q")

        if query:
            queryset = queryset.filter(name__icontains=query).order_by(
                "-last_year", "name", "id"
            )
        return queryset
