from django.db import models


class PlayerInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    fplayerid = models.IntegerField(blank=True, null=True)
    first_year = models.IntegerField(blank=True, null=True)
    last_year = models.IntegerField(blank=True, null=True)
    default_batting = models.IntegerField(blank=True, null=True)
    bat_career = models.FloatField(blank=True, null=True)
    bat_peak = models.FloatField(blank=True, null=True)
    bat_avg = models.FloatField(blank=True, null=True)
    career_pas = models.IntegerField(blank=True, null=True)
    peak_pas = models.IntegerField(blank=True, null=True)
    bat_rate_career = models.FloatField(blank=True, null=True)
    bat_rate_peak = models.FloatField(blank=True, null=True)
    bat_rate_avg = models.FloatField(blank=True, null=True)
    pit_career = models.FloatField(blank=True, null=True)
    pit_peak = models.FloatField(blank=True, null=True)
    pit_avg = models.FloatField(blank=True, null=True)
    pit_rate_career = models.FloatField(blank=True, null=True)
    pit_rate_peak = models.FloatField(blank=True, null=True)
    pit_rate_avg = models.FloatField(blank=True, null=True)
    career_ip = models.FloatField(blank=True, null=True)
    peak_ip = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "player_info"


class Batters(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    pa = models.IntegerField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    r = models.IntegerField(blank=True, null=True)
    rbi = models.IntegerField(blank=True, null=True)
    sb = models.IntegerField(blank=True, null=True)
    bb_rate = models.FloatField(blank=True, null=True)
    k_rate = models.FloatField(blank=True, null=True)
    iso = models.FloatField(blank=True, null=True)
    babip = models.FloatField(blank=True, null=True)
    avg = models.FloatField(blank=True, null=True)
    obp = models.FloatField(blank=True, null=True)
    slg = models.FloatField(blank=True, null=True)
    woba = models.FloatField(blank=True, null=True)
    wrc_plus = models.IntegerField(blank=True, null=True)
    ev = models.FloatField(blank=True, null=True)
    bsr = models.FloatField(blank=True, null=True)
    off = models.FloatField(blank=True, null=True)
    def_field = models.FloatField(
        db_column="def", blank=True, null=True
    )  # Field renamed because it was a Python reserved word.
    war = models.FloatField(blank=True, null=True)
    war_per_600 = models.FloatField(blank=True, null=True)
    player = models.ForeignKey(
        "PlayerInfo",
        related_name="batting_stats",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "batters"


class Pitchers(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    w = models.IntegerField(blank=True, null=True)
    l = models.IntegerField(blank=True, null=True)
    sv = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    gs = models.IntegerField(blank=True, null=True)
    ip = models.FloatField(blank=True, null=True)
    k_per_9 = models.FloatField(blank=True, null=True)
    bb_per_9 = models.FloatField(blank=True, null=True)
    hr_per_9 = models.FloatField(blank=True, null=True)
    babip = models.FloatField(blank=True, null=True)
    lob_rate = models.FloatField(blank=True, null=True)
    gb_rate = models.FloatField(blank=True, null=True)
    hr_per_fb = models.FloatField(blank=True, null=True)
    ev = models.FloatField(blank=True, null=True)
    era = models.FloatField(blank=True, null=True)
    fip = models.FloatField(blank=True, null=True)
    xfip = models.FloatField(blank=True, null=True)
    war = models.FloatField(blank=True, null=True)
    war_per_200 = models.FloatField(blank=True, null=True)
    player = models.ForeignKey(
        "PlayerInfo",
        related_name="pitching_stats",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "pitchers"
