"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from rest_framework_mvt.views import mvt_view_factory
from . import views
from .models import ncwellwise_subset_20102019_geom, acs_2019_5y_estimates_geom, ejscreen_subset_geom, nc_covid_zipcode_geom, nc_preterm_subset_geom, nc_wildfires_geom, ncdot_county_boundaries, nc_superfund_sites, hospitals_4326, public_schools_4326, non_public_schools_4326

router = routers.DefaultRouter()
router.register(r'nc_superfund_sites', views.drf_nc_superfund_sites_View)
router.register(r'hospitals_4326', views.drf_hospitals_4326_View)
router.register(r'public_schools_4326', views.drf_public_schools_4326_View)
router.register(r'non_public_schools_4326', views.drf_non_public_schools_4326_View)

urlpatterns = [
    path("api/", include(router.urls)),
    path("apimvt/v1/data/ncwellwise_subset_20102019_geom.mvt/", mvt_view_factory(ncwellwise_subset_20102019_geom)),
    path("apimvt/v1/data/acs_2019_5y_estimates_geom.mvt/", mvt_view_factory(acs_2019_5y_estimates_geom)),
    path("apimvt/v1/data/ejscreen_subset_geom.mvt/", mvt_view_factory(ejscreen_subset_geom)),
    path("apimvt/v1/data/nc_covid_zipcode_geom.mvt/", mvt_view_factory(nc_covid_zipcode_geom)),
    path("apimvt/v1/data/nc_preterm_subset_geom.mvt/", mvt_view_factory(nc_preterm_subset_geom)),
    path("apimvt/v1/data/nc_wildfires_geom.mvt/", mvt_view_factory(nc_wildfires_geom)),
    path("apimvt/v1/data/ncdot_county_boundaries.mvt/", mvt_view_factory(ncdot_county_boundaries)),
    path("apimvt/v1/data/nc_superfund_sites.mvt/", mvt_view_factory(nc_superfund_sites)),
    path("apimvt/v1/data/hospitals_4326.mvt/", mvt_view_factory(hospitals_4326)),
    path("apimvt/v1/data/public_schools_4326.mvt/", mvt_view_factory(public_schools_4326)),
    path("apimvt/v1/data/non_public_schools_4326.mvt/", mvt_view_factory(non_public_schools_4326)),
]
