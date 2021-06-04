#from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import ncwellwise_subset_20102019, ltdb_std_2012_sample_subset, acs_2019_5y_estimates, ejscreen_subset, nc_covid_zipcode, triangle_tracts, nc_census_tracks_4326, nc_census_bg_4326, ncwellwise_triangle_20102019_geom, ncwellwise_subset_20102019_geom, ltdb_std_2012_sample_subset_geom, acs_2019_5y_estimates_geom, ejscreen_subset_geom, nc_covid_zipcode_geom, ncdot_county_boundaries
from drf_queryfields import QueryFieldsMixin

class ncwellwise_subset_20102019_Serializer(QueryFieldsMixin,):
    class Meta:
        model = ncwellwise_subset_20102019
        id_field = 'id'
        fields = ('id', 'geoid10','arsenic_mean','arsenic_med','arsenic_prcast','arsenic_minimum','arsenic_maximum','arsenic_std','cadmium_mean','cadmium_med','cadmium_prcast','cadmium_minimum','cadmium_maximum','cadmium_std','lead_mean','lead_med','lead_prcast','lead_minimum','lead_maximum','lead_std','manganese_mean','manganese_med','manganese_prcast','manganese_minimum','manganese_maximum','manganese_std')

class ltdb_std_2012_sample_subset_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = ncwellwise_subset_20102019
        id_field = 'id'
        fields = ('id', 'geoid10','pnhwht12','pnhblk12','phisp12','pasian12','pntv12','hincw12','hincb12','hinch12','hinca12','pwpov12','pbpov12','phpov12','papov12','pnapov12')

class acs_2019_5y_estimates_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = acs_2019_5y_estimates_geom
        id_field = 'id'
        fields = ('id','geoid10','percent_below_poverty_level','speak_a_language_other_than_english','two_or_more_races','asian_alone','american_indian_and_alaska_native_alone','native_hawaiian_and_other_pacific_islander_alone','white_alone','black_or_african_american_alone','not_hispanic_or_latino','hispanic_or_latino_of_any_race')

class ejscreen_subset_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = ejscreen_subset
        id_field = 'id'
        fields = ('id','geoid10','d_ldpnt_2','d_dslpm_2','d_cancr_2','d_resp_2','d_ptraf_2','d_pwdis_2','d_pnpl_2','d_prmp_2','d_ptsdf_2','d_ozone_2','d_pm25_2')

class nc_covid_zipcode_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    model = nc_covid_zipcode
    id_field = 'id'
    fields = ('id','zipcode','cases,cases_per_10000_res','cases_per_100000_res','deaths')

class triangle_tracts_Serializer(QueryFieldsMixin,):
    class Meta:
        model = triangle_tracts
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'statefp10', 'countyfp10', 'tractce10', 'geoid10', 'name10', 'namelsad10', 'mtfcc10', 'funcstat10', 'aland10', 'awater10', 'intptlat10', 'intptlon10', 'layer', 'path')

class nc_census_tracks_4326_Serializer(QueryFieldsMixin,):
    class Meta:
        model = nc_census_tracks_4326
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'geoid10', 'total_pop', 'onemapsdea', 'shapestare', 'shapestlen')

class nc_census_bg_4326_Serializer(QueryFieldsMixin,):
    class Meta:
        model = nc_census_bg_4326
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'geoid10', 'total_pop', 'onemapsdea', 'shapestare', 'shapestlen')

class ncwellwise_triangle_20102019_geom_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = ncwellwise_triangle_20102019_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'geoid10','arsenic_mean','arsenic_med','arsenic_prcast','arsenic_minimum','arsenic_maximum','arsenic_std','cadmium_mean','cadmium_med','cadmium_prcast','cadmium_minimum','cadmium_maximum','cadmium_std','lead_mean','lead_med','lead_prcast','lead_minimum','lead_maximum','lead_std','manganese_mean','manganese_med','manganese_prcast','manganese_minimum','manganese_maximum','manganese_std')

class ncwellwise_subset_20102019_geom_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = ncwellwise_subset_20102019_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'geoid10','arsenic_mean','arsenic_med','arsenic_prcast','arsenic_minimum','arsenic_maximum','arsenic_std','cadmium_mean','cadmium_med','cadmium_prcast','cadmium_minimum','cadmium_maximum','cadmium_std','lead_mean','lead_med','lead_prcast','lead_minimum','lead_maximum','lead_std','manganese_mean','manganese_med','manganese_prcast','manganese_minimum','manganese_maximum','manganese_std')

class ltdb_std_2012_sample_subset_geom_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = ltdb_std_2012_sample_subset_geom 
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'geoid10','pnhwht12','pnhblk12','phisp12','pasian12','pntv12','hincw12','hincb12','hinch12','hinca12','pwpov12','pbpov12','phpov12','papov12','pnapov12')

class acs_2019_5y_estimates_geom_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = acs_2019_5y_estimates_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','geoid10','percent_below_poverty_level','speak_a_language_other_than_english','two_or_more_races','asian_alone','american_indian_and_alaska_native_alone','native_hawaiian_and_other_pacific_islander_alone','white_alone','black_or_african_american_alone','not_hispanic_or_latino','hispanic_or_latino_of_any_race')

class ejscreen_subset_geom_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = ejscreen_subset_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','geoid10','d_ldpnt_2','d_dslpm_2','d_cancr_2','d_resp_2','d_ptraf_2','d_pwdis_2','d_pnpl_2','d_prmp_2','d_ptsdf_2','d_ozone_2','d_pm25_2')

class nc_covid_zipcode_geom_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    model = nc_covid_zipcode_geom
    geo_field = 'geom'
    id_field = 'id'
    fields = ('id','zipcode','cases,cases_per_10000_res','cases_per_100000_res','deaths')

class ncdot_county_boundaries_Serializer(QueryFieldsMixin,GeoFeatureModelSerializer):
    class Meta:
        model = ncdot_county_boundaries
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','objectid','fips','countyname','uppercount','sapcountyi','dotdistric','dotdivisio','sap_cnty_n','cnty_nbr','dstrct_nbr','div_nbr','name','shapestare','shapestlen')

