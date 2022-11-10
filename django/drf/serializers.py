#from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer #ModelSerializer
from .models import ncwellwise_subset_20102019_geom, acs_2019_5y_estimates_geom, ejscreen_subset_geom, nc_covid_zipcode_geom, nc_preterm_subset_geom, nc_wildfires_geom, ncdot_county_boundaries, nc_superfund_sites, hospitals_4326, public_schools_4326, non_public_schools_4326

class ncwellwise_subset_20102019_geom_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = ncwellwise_subset_20102019_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id', 'geoid10','arsenic_mean','arsenic_med','arsenic_prcast','arsenic_minimum','arsenic_maximum','arsenic_std','cadmium_mean','cadmium_med','cadmium_prcast','cadmium_minimum','cadmium_maximum','cadmium_std','lead_mean','lead_med','lead_prcast','lead_minimum','lead_maximum','lead_std','manganese_mean','manganese_med','manganese_prcast','manganese_minimum','manganese_maximum','manganese_std')

class acs_2019_5y_estimates_geom_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = acs_2019_5y_estimates_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','geoid10','percent_below_poverty_level','speak_a_language_other_than_english','two_or_more_races','asian_alone','american_indian_and_alaska_native_alone','native_hawaiian_and_other_pacific_islander_alone','white_alone','black_or_african_american_alone','not_hispanic_or_latino','hispanic_or_latino_of_any_race')

class ejscreen_subset_geom_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = ejscreen_subset_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','geoid10','d_ldpnt_2','d_dslpm_2','d_cancr_2','d_resp_2','d_ptraf_2','d_pwdis_2','d_pnpl_2','d_prmp_2','d_ptsdf_2','d_ozone_2','d_pm25_2')

class nc_covid_zipcode_geom_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = nc_covid_zipcode_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','zipcode','cases,cases_per_10000_res','cases_per_100000_res','deaths')

class nc_preterm_subset_geom_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = nc_preterm_subset_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','geoid10','fc_calcega_mean_avg','fc_calcega_med','fc_calcpreterm_percentage','fc_clinega_mean_avg','fc_clinega_med','fc_clinpreterm_percentage','sc_calcega_mean_avg,sc_calcega_med','sc_calcpreterm_percentage','sc_clinega_mean_avg','sc_clinega_med','sc_clinpreterm_percentage')

class nc_wildfires_geom_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = nc_wildfires_geom
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','geoid20','wildfire_haz_pot_qnum','wildfire_haz_pot_qprcnt')

class ncdot_county_boundaries_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = ncdot_county_boundaries
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','objectid','fips','countyname','uppercount','sapcountyi','dotdistric','dotdivisio','sap_cnty_n','cnty_nbr','dstrct_nbr','div_nbr','name','shapestare','shapestlen')

class nc_superfund_sites_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = nc_superfund_sites
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','superfund_site','city','county','state','country','region','year_proposed','year_listed','year_complete','year_deleted','years_listed_current','years_listed_deleted','partial_deletion','hazard_rank_sys_score','status','latitude','longitude','geom')

class hospitals_4326_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = hospitals_4326
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','objectid','facility','licensee','expires','hgenlic','rehabhlic','psylic','salic','detoxlic','hoslic','rsrchlic','nfgenlic','othrhlic','alzlic','hivlic','tbilic','venlic','othnflic','rehabnlic','haalzlic','hahivlic','hagenlic','orheart_hl','orcsect_hl','orother_hl','oramsu_hl','orshare_hl','orendo_hl','altfacname','hltype','stype','fcounty','fcity','fstate','fzip','faddr1','fphone','licno','geom')

class public_schools_4326_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = public_schools_4326
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','objectid','lea_school','ptmoved','comments','reviewed','school_nam','principal','street_lon','phys_addr','phys_city','phys_zip','phone','mail_addr','mail_city','mail_zip','fax','url_addres','county','accr_stat','sch_desg','sch_type','sch_ptype','sch_ctype','ext_hours','num_teach','bgn_grade','end_grade','pre_k','elem','middle','high','early_coll','geom')

class non_public_schools_4326_Serializer(HyperlinkedModelSerializer,GeoFeatureModelSerializer):
    class Meta:
        model = non_public_schools_4326
        geo_field = 'geom'
        id_field = 'id'
        fields = ('id','objectid_1','objectid','schoolid','county','schoolname','address','city','state','zipcode','website','schooltype','geom')
