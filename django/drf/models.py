from __future__ import unicode_literals
from django.contrib.gis.db import models
from rest_framework_mvt.managers import MVTManager
from django.db import models as omodels

# Create your models here.
STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published')
)

# Create your models here.
class ncwellwise_subset_20102019(models.Model):
    geoid10 = models.TextField(11,null=False)
    arsenic_mean = models.FloatField(null=True)
    arsenic_med = models.FloatField(null=True)
    arsenic_prcast = models.FloatField(null=True)
    arsenic_minimum = models.FloatField(null=True)
    arsenic_maximum = models.FloatField(null=True)
    arsenic_std = models.FloatField(null=True) 
    cadmium_mean = models.FloatField(null=True)
    cadmium_med = models.FloatField(null=True)
    cadmium_prcast = models.FloatField(null=True)
    cadmium_minimum = models.FloatField(null=True)
    cadmium_maximum = models.FloatField(null=True)
    cadmium_std = models.FloatField(null=True)
    lead_mean = models.FloatField(null=True)
    lead_med = models.FloatField(null=True)
    lead_prcast = models.FloatField(null=True)
    lead_minimum = models.FloatField(null=True)
    lead_maximum = models.FloatField(null=True)
    lead_std = models.FloatField(null=True)
    manganese_mean = models.FloatField(null=True)
    manganese_med = models.FloatField(null=True)
    manganese_prcast = models.FloatField(null=True)
    manganese_minimum = models.FloatField(null=True)
    manganese_maximum = models.FloatField(null=True)
    manganese_std = models.FloatField(null=True)

class acs_2019_5y_estimates(models.Model):
    geoid10 = models.TextField(2,null=False)
    percent_below_poverty_level = models.FloatField(null=True)
    speak_a_language_other_than_english = models.FloatField(null=True)
    two_or_more_races = models.FloatField(null=True)
    asian_alone = models.FloatField(null=True)
    american_indian_and_alaska_native_alone = models.FloatField(null=True)
    native_hawaiian_and_other_pacific_islander_alone = models.FloatField(null=True)
    white_alone = models.FloatField(null=True)
    black_or_african_american_alone = models.FloatField(null=True)
    not_hispanic_or_latino = models.FloatField(null=True)
    hispanic_or_latino_of_any_race = models.FloatField(null=True)

class ejscreen_subset(models.Model):
    geoid10 = models.TextField(12,null=False)
    d_ldpnt_2 = models.FloatField(null=True)
    d_dslpm_2 = models.FloatField(null=True)
    d_cancr_2 = models.FloatField(null=True)
    d_resp_2 = models.FloatField(null=True)
    d_ptraf_2 = models.FloatField(null=True)
    d_pwdis_2 = models.FloatField(null=True)
    d_pnpl_2 = models.FloatField(null=True)
    d_prmp_2 = models.FloatField(null=True)
    d_ptsdf_2 = models.FloatField(null=True)
    d_ozone_2 = models.FloatField(null=True)
    d_pm25_2 = models.FloatField(null=True)

class nc_covid_zipcode(models.Model):
    zipcode = models.TextField(5,null=False)
    cases = models.IntegerField()
    cases_per_10000_res = models.FloatField(null=True)
    cases_per_100000_res = models.FloatField(null=True) 
    deaths = models.IntegerField()

class nc_preterm_subset(models.Model):
    geoid10 = models.TextField(11, null=True)
    fc_calcega_mean_avg = models.FloatField(null=True)
    fc_calcega_med = models.FloatField(null=True) 
    fc_calcpreterm_percentage = models.FloatField(null=True)
    fc_clinega_mean_avg = models.FloatField(null=True)
    fc_clinega_med = models.FloatField(null=True)
    fc_clinpreterm_percentage = models.FloatField(null=True)
    sc_calcega_mean_avg = models.FloatField(null=True)
    sc_calcega_med = models.FloatField(null=True)
    sc_calcpreterm_percentage = models.FloatField(null=True)
    sc_clinega_mean_avg = models.FloatField(null=True)
    sc_clinega_med = models.FloatField(null=True)
    sc_clinpreterm_percentage = models.FloatField(null=True)

class nc_census_tracks_4326(models.Model):
    geoid10 = models.TextField(11, null=True)
    total_pop = models.IntegerField()
    onemapsdea = models.IntegerField()
    shapestare = models.FloatField(null=True)
    shapestlen = models.FloatField(null=True)
    geom = models.MultiPolygonField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

class nc_census_bg_4326(models.Model):
    geoid10 = models.TextField(11, null=True)
    total_pop = models.IntegerField()
    onemapsdea = models.IntegerField()
    shapestare = models.FloatField(null=True)
    shapestlen = models.FloatField(null=True)
    geom = models.MultiPolygonField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

class zip_code_areas_4326(models.Model):
    objectid = models.IntegerField()
    zcta5ce10 = models.TextField(5,null=True)
    affgeoid10 = models.TextField(14,null=True)
    geoid10 = models.TextField(5,null=True)
    aland10 = models.IntegerField()
    awater10 = models.IntegerField()
    shapestare = models.FloatField(null=True)
    shapestlen = models.FloatField(null=True)
    geom = models.MultiPolygonField(null=True)
    #vector_tiles = MVTManager()
    objects = models.Manager()
    vector_tiles = MVTManager()

class ncdot_county_boundaries(models.Model):
    objectid = models.IntegerField()
    fips = models.IntegerField() 
    countyname = models.TextField(12,null=True) 
    uppercount = models.TextField(12,null=True)
    sapcountyi = models.TextField(3,null=True) 
    dotdistric = models.IntegerField() 
    dotdivisio = models.IntegerField() 
    sap_cnty_n = models.IntegerField() 
    cnty_nbr = models.IntegerField() 
    dstrct_nbr = models.IntegerField() 
    div_nbr = models.IntegerField() 
    name = models.TextField(12,null=True) 
    shapestare = models.FloatField(null=True) 
    shapestlen = models.FloatField(null=True) 
    geom = models.MultiLineStringField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

class ncwellwise_subset_20102019_geom(models.Model):
    geoid10 = models.TextField(2,null=False)
    arsenic_mean = models.FloatField(null=True)
    arsenic_med = models.FloatField(null=True)
    arsenic_prcast = models.FloatField(null=True)
    arsenic_minimum = models.FloatField(null=True)
    arsenic_maximum = models.FloatField(null=True)
    arsenic_std = models.FloatField(null=True)
    cadmium_mean = models.FloatField(null=True)
    cadmium_med = models.FloatField(null=True)
    cadmium_prcast = models.FloatField(null=True)
    cadmium_minimum = models.FloatField(null=True)
    cadmium_maximum = models.FloatField(null=True)
    cadmium_std = models.FloatField(null=True)
    lead_mean = models.FloatField(null=True)
    lead_med = models.FloatField(null=True)
    lead_prcast = models.FloatField(null=True)
    lead_minimum = models.FloatField(null=True)
    lead_maximum = models.FloatField(null=True)
    lead_std = models.FloatField(null=True)
    manganese_mean = models.FloatField(null=True)
    manganese_med = models.FloatField(null=True)
    manganese_prcast = models.FloatField(null=True)
    manganese_minimum = models.FloatField(null=True)
    manganese_maximum = models.FloatField(null=True)
    manganese_std = models.FloatField(null=True)
    geom = models.MultiPolygonField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = "drf_ncwellwise_subset_20102019_geom"

class acs_2019_5y_estimates_geom(models.Model):
    geoid10 = models.TextField(2,null=False)
    percent_below_poverty_level = models.FloatField(null=True)
    speak_a_language_other_than_english = models.FloatField(null=True)
    two_or_more_races = models.FloatField(null=True)
    asian_alone = models.FloatField(null=True)
    american_indian_and_alaska_native_alone = models.FloatField(null=True)
    native_hawaiian_and_other_pacific_islander_alone = models.FloatField(null=True)
    white_alone = models.FloatField(null=True)
    black_or_african_american_alone = models.FloatField(null=True)
    not_hispanic_or_latino = models.FloatField(null=True)
    hispanic_or_latino_of_any_race = models.FloatField(null=True)
    geom = models.MultiPolygonField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = "drf_acs_2019_5y_estimates_geom"

class ejscreen_subset_geom(models.Model):
    geoid10 = models.TextField(12,null=False)
    d_ldpnt_2 = models.FloatField(null=True)
    d_dslpm_2 = models.FloatField(null=True)
    d_cancr_2 = models.FloatField(null=True)
    d_resp_2 = models.FloatField(null=True)
    d_ptraf_2 = models.FloatField(null=True)
    d_pwdis_2 = models.FloatField(null=True)
    d_pnpl_2 = models.FloatField(null=True)
    d_prmp_2 = models.FloatField(null=True)
    d_ptsdf_2 = models.FloatField(null=True)
    d_ozone_2 = models.FloatField(null=True)
    d_pm25_2 = models.FloatField(null=True)
    geom = models.MultiPolygonField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = "drf_ejscreen_subset_geom"

class nc_covid_zipcode_geom(models.Model):
    zipcode = models.TextField(5,null=False) 
    cases = models.IntegerField()
    cases_per_10000_res = models.FloatField(null=True)
    cases_per_100000_res = models.FloatField(null=True)
    deaths = models.IntegerField()
    geom = models.MultiPolygonField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = "drf_nc_covid_zipcode_geom"

class nc_preterm_subset_geom(models.Model):
    geoid10 = models.TextField(11, null=True)
    fc_calcega_mean_avg = models.FloatField(null=True)
    fc_calcega_med = models.FloatField(null=True)
    fc_calcpreterm_percentage = models.FloatField(null=True)
    fc_clinega_mean_avg = models.FloatField(null=True)
    fc_clinega_med = models.FloatField(null=True)
    fc_clinpreterm_percentage = models.FloatField(null=True)
    sc_calcega_mean_avg = models.FloatField(null=True)
    sc_calcega_med = models.FloatField(null=True)
    sc_calcpreterm_percentage = models.FloatField(null=True)
    sc_clinega_mean_avg = models.FloatField(null=True)
    sc_clinega_med = models.FloatField(null=True) 
    sc_clinpreterm_percentage = models.FloatField(null=True)
    geom = models.MultiPolygonField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = "drf_nc_preterm_subset_geom"

class nc_superfund_sites(models.Model):
    superfund_site = models.TextField(55, null=True)
    city = models.TextField(15, null=True)
    county = models.TextField(16, null=True)
    state = models.TextField(2, null=True)
    country = models.TextField(2, null=True)
    region = models.IntegerField()
    year_proposed = models.FloatField()
    year_listed = models.FloatField()
    year_complete = models.FloatField()
    year_deleted = models.TextField(12, null=True)
    years_listed_current = models.TextField(17, null=True)
    years_listed_deleted = models.TextField(17, null=True)
    partial_deletion = models.TextField(4, null=True)
    hazard_rank_sys_score = models.FloatField(null=True)
    status = models.TextField(31, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    geom = models.PointField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

