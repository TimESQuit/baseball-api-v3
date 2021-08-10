from django.urls import path, re_path

from .views import Leaderboards, PlayerDetail, PlayerSearch

app_name = "baseball"

urlpatterns = [
    re_path(
        r"(?P<when_player>[\w]*)-(?P<player_type>[\w]*)-leaders/",
        Leaderboards.as_view(),
        name="leaderboards",
    ),
    path("players/<int:pk>/", PlayerDetail.as_view(), name="batter-detail"),
    path("players/search", PlayerSearch.as_view(), name="player-search"),
]
