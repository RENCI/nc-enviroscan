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

class ltdb_std_2012_sample_subset(models.Model):
    geoid10 = models.TextField(11,null=False)
    pnhwht12 = models.FloatField(null=True)
    pnhblk12 = models.FloatField(null=True)
    phisp12 = models.FloatField(null=True)
    pasian12 = models.FloatField(null=True)
    pntv12 = models.FloatField(null=True)
    hincw12 = models.FloatField(null=True)
    hincb12 = models.FloatField(null=True)
    hinch12 = models.FloatField(null=True)
    hinca12 = models.FloatField(null=True)
    pwpov12 = models.FloatField(null=True)
    pbpov12 = models.FloatField(null=True)
    phpov12 = models.FloatField(null=True)
    papov12 = models.FloatField(null=True)
    pnapov12 = models.FloatField(null=True)

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

class triangle_tracts(models.Model):
    geom = models.MultiPolygonField(null=True)
    statefp10 = models.TextField(2,null=True)
    countyfp10 = models.TextField(3,null=True)
    tractce10 = models.TextField(6,null=True)
    geoid10 = models.TextField(11,null=True)
    name10 = models.TextField(7,null=True)
    namelsad10 = models.TextField(20,null=True)
    mtfcc10 = models.TextField(5,null=True)
    funcstat10 = models.TextField(1,null=True)
    aland10 = models.FloatField(null=True)
    awater10 = models.FloatField(null=True)
    intptlat10 = models.TextField(11,null=True)
    intptlon10 = models.TextField(12,null=True)
    layer = models.TextField(254,null=True)
    path = models.TextField(254,null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

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
    #vector_tiles = MVTManager()
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

class ncwellwise_triangle_20102019_geom(models.Model):
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

    class Meta:
        managed = False
        db_table = "drf_ncwellwise_triangle_20102019_geom"

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

class ltdb_std_2012_sample_subset_geom(models.Model):
    geoid10 = models.TextField(2,null=False)
    pnhwht12 = models.FloatField(null=True)
    pnhblk12 = models.FloatField(null=True)
    phisp12 = models.FloatField(null=True)
    pasian12 = models.FloatField(null=True)
    pntv12 = models.FloatField(null=True)
    hincw12 = models.FloatField(null=True)
    hincb12 = models.FloatField(null=True)
    hinch12 = models.FloatField(null=True)
    hinca12 = models.FloatField(null=True)
    pwpov12 = models.FloatField(null=True)
    pbpov12 = models.FloatField(null=True)
    phpov12 = models.FloatField(null=True)
    papov12 = models.FloatField(null=True)
    pnapov12 = models.FloatField(null=True)
    geom = models.MultiPolygonField(null=True)
    objects = models.Manager()
    vector_tiles = MVTManager()

    class Meta:
        managed = False
        db_table = "drf_ltdb_std_2012_sample_subset_geom"

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

