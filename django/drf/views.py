from __future__ import unicode_literals
from rest_framework import viewsets
from .serializers import ncwellwise_subset_20102019_geom_Serializer, acs_2019_5y_estimates_geom_Serializer, ejscreen_subset_geom_Serializer, nc_covid_zipcode_geom_Serializer, nc_preterm_subset_geom_Serializer, ncdot_county_boundaries_Serializer, nc_superfund_sites_Serializer
from .models import ncwellwise_subset_20102019_geom, acs_2019_5y_estimates_geom, ejscreen_subset_geom, nc_covid_zipcode_geom, nc_preterm_subset_geom, ncdot_county_boundaries, nc_superfund_sites

class drf_ncwellwise_subset_20102019_geom_View(viewsets.ModelViewSet):
    queryset = ncwellwise_subset_20102019_geom.objects.all()
    serializer_class = ncwellwise_subset_20102019_geom_Serializer

class drf_acs_2019_5y_estimates_geom_View(viewsets.ModelViewSet):
    queryset = acs_2019_5y_estimates_geom.objects.all()
    serializer_class = acs_2019_5y_estimates_geom_Serializer

class drf_ejscreen_subset_geom_View(viewsets.ModelViewSet):
    queryset = ejscreen_subset_geom.objects.all()
    serializer_class = ejscreen_subset_geom_Serializer

class drf_nc_covid_zipcode_geom_View(viewsets.ModelViewSet):
    queryset = nc_covid_zipcode_geom.objects.all()
    serializer_class = nc_covid_zipcode_geom_Serializer

class drf_nc_preterm_subset_geom_View(viewsets.ModelViewSet):
    queryset = nc_preterm_subset_geom.objects.all()
    serializer_class = nc_preterm_subset_geom_Serializer

class drf_ncdot_county_boundaries_View(viewsets.ModelViewSet):
    queryset = ncdot_county_boundaries.objects.all()
    serializer_class = ncdot_county_boundaries_Serializer

class drf_nc_superfund_sites_View(viewsets.ModelViewSet):
    queryset = nc_superfund_sites.objects.all()
    serializer_class = nc_superfund_sites_Serializer

