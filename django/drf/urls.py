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
from .models import ncwellwise_subset_20102019_geom, acs_2019_5y_estimates_geom, ejscreen_subset_geom, nc_covid_zipcode_geom, nc_preterm_subset_geom, ncdot_county_boundaries

router = routers.DefaultRouter()
router.register(r'ncwellwise_subset_20102019_geom', views.drf_ncwellwise_subset_20102019_geom_View)
router.register(r'acs_2019_5y_estimates_geom', views.drf_acs_2019_5y_estimates_geom_View)
router.register(r'ejscreen_subset_geom', views.drf_ejscreen_subset_geom_View)
router.register(r'nc_covid_zipcode_geom', views.drf_nc_covid_zipcode_geom_View)
router.register(r'nc_preterm_subset_geom', views.drf_nc_preterm_subset_geom_View)
router.register(r'ncdot_county_boundaries', views.drf_ncdot_county_boundaries_View)

urlpatterns = [
    path("api/", include(router.urls)),
    path("apimvt/v1/data/ncwellwise_subset_20102019_geom.mvt/", mvt_view_factory(ncwellwise_subset_20102019_geom)),
    path("apimvt/v1/data/acs_2019_5y_estimates_geom.mvt/", mvt_view_factory(acs_2019_5y_estimates_geom)),
    path("apimvt/v1/data/ejscreen_subset_geom.mvt/", mvt_view_factory(ejscreen_subset_geom)),
    path("apimvt/v1/data/nc_covid_zipcode_geom.mvt/", mvt_view_factory(nc_covid_zipcode_geom)),
    path("apimvt/v1/data/nc_preterm_subset_geom.mvt/", mvt_view_factory(nc_preterm_subset_geom)),
    path("apimvt/v1/data/ncdot_county_boundaries.mvt/", mvt_view_factory(ncdot_county_boundaries)),
]
