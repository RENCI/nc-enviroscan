from __future__ import unicode_literals
import os
import jwt
import json
from functools import wraps
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from six.moves.urllib import request as req
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
from .serializers import ncwellwise_triangle_20102019_geom_Serializer, ncwellwise_subset_20102019_geom_Serializer, ltdb_std_2012_sample_subset_geom_Serializer, acs_2019_5y_estimates_geom_Serializer, ejscreen_subset_geom_Serializer, nc_covid_zipcode_geom_Serializer, ncdot_county_boundaries_Serializer
from .models import ncwellwise_triangle_20102019_geom, ncwellwise_subset_20102019_geom, ltdb_std_2012_sample_subset_geom, acs_2019_5y_estimates_geom, ejscreen_subset_geom, nc_covid_zipcode_geom, ncdot_county_boundaries
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework_gis.filters import InBBoxFilter

def get_token_auth_header(request):
    #Obtains the access token from the Authorization Header
    auth = request.META.get("HTTP_AUTHORIZATION", None)
    parts = auth.split()
    token = parts[1]

    return token

def requires_scope(required_scope):
    #Determines if the required scope is present in the access token
    #Args:
    #    required_scope (str): The scope required to access the resource
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = get_token_auth_header(args[0])
            AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
            API_IDENTIFIER = os.environ.get('API_IDENTIFIER')
            jsonurl = req.urlopen('https://' + AUTH0_DOMAIN + '/.well-known/jwks.json')
            jwks = json.loads(jsonurl.read())
            cert = '-----BEGIN CERTIFICATE-----\n' + jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'
            certificate = load_pem_x509_certificate(cert.encode('utf-8'), default_backend())
            public_key = certificate.public_key()
            decoded = jwt.decode(token, public_key, audience=API_IDENTIFIER, algorithms=['RS256'])

            if decoded.get("scope"):
                token_scopes = decoded["scope"].split()
                for token_scope in token_scopes:
                    if token_scope == required_scope:
                        return f(*args, **kwargs)
            response = JsonResponse({'message': 'You don\'t have access to this resource'})
            response.status_code = 403
            return response
        return decorated
    return require_scope

@csrf_exempt
@api_view(['GET', 'POST'])
def ncwellwise_subset_20102019_geom_list(request):
    #List ncwellwise_subset_20102019_geom, or create a new ncwellwise_subset_20102019_geom.
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        ncwellwise_subset_20102019 = ncwellwise_subset_20102019_geom.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(ncwellwise_subset_20102019, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = ncwellwise_subset_20102019_geom_Serializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/ncwellwise_subset_20102019_geom/?page=' + str(nextPage), 'prevlink': '/api/ncwellwise_subset_20102019_geom/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = ncwellwise_subset_20102019_geom_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ncwellwise_subset_20102019_geom_detail(request, id):
    #Retrieve, update or delete a ncwellwise_subset_20102019_geom instance.
    try:
        ncwellwise_subset_20102019 = ncwellwise_subset_20102019_geom.objects.get(id=id)
    except ncwellwise_subset_20102019.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ncwellwise_subset_20102019_geom_Serializer(ncwellwise_subset_20102019, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ncwellwise_subset_20102019_geom_Serializer(ncwellwise_subset_20102019, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ncwellwise_subset_20102019.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class drf_ncwellwise_triangle_20102019_geom_View(viewsets.ModelViewSet):
    queryset = ncwellwise_triangle_20102019_geom.objects.all()
    serializer_class = ncwellwise_triangle_20102019_geom_Serializer
    bbox_filter_field = 'geom'
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    fileter_fields = ['id', 'geoid10','arsenic_mean','arsenic_med','arsenic_prcast','arsenic_minimum','arsenic_maximum','arsenic_std','cadmium_mean','cadmium_med','cadmium_prcast','cadmium_minimum','cadmium_maximum','cadmium_std','lead_mean','lead_med','lead_prcast','lead_minimum','lead_maximum','lead_std','manganese_mean','manganese_med','manganese_prcast','manganese_minimum','manganese_maximum','manganese_std']
    bbox_filter_include_overlapping = True

class drf_ncwellwise_subset_20102019_geom_View(viewsets.ModelViewSet):
    queryset = ncwellwise_subset_20102019_geom.objects.all()
    serializer_class = ncwellwise_subset_20102019_geom_Serializer
    bbox_filter_field = 'geom'
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    fileter_fields = ['id', 'geoid10','arsenic_mean','arsenic_med','arsenic_prcast','arsenic_minimum','arsenic_maximum','arsenic_std','cadmium_mean','cadmium_med','cadmium_prcast','cadmium_minimum','cadmium_maximum','cadmium_std','lead_mean','lead_med','lead_prcast','lead_minimum','lead_maximum','lead_std','manganese_mean','manganese_med','manganese_prcast','manganese_minimum','manganese_maximum','manganese_std']
    bbox_filter_include_overlapping = True

class drf_ltdb_std_2012_sample_subset_geom_View(viewsets.ModelViewSet):
    queryset = ltdb_std_2012_sample_subset_geom.objects.all()
    serializer_class = ltdb_std_2012_sample_subset_geom_Serializer
    bbox_filter_field = 'geom'
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    fileter_fields = ['id', 'geoid10','pnhwht12','pnhblk12','phisp12','pasian12','pntv12','hincw12','hincb12','hinch12','hinca12','pwpov12','pbpov12','phpov12','papov12','pnapov12']
    bbox_filter_include_overlapping = True

class drf_acs_2019_5y_estimates_geom_View(viewsets.ModelViewSet):
    queryset = acs_2019_5y_estimates_geom.objects.all()
    serializer_class = acs_2019_5y_estimates_geom_Serializer
    bbox_filter_field = 'geom'
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    fileter_fields = ['id', 'geoid10','percent_below_poverty_level','speak_a_language_other_than_english','two_or_more_races','asian_alone','american_indian_and_alaska_native_alone','native_hawaiian_and_other_pacific_islander_alone','white_alone','black_or_african_american_alone','not_hispanic_or_latino','hispanic_or_latino_of_any_race']
    bbox_filter_include_overlapping = True

class drf_ejscreen_subset_geom_View(viewsets.ModelViewSet):
    queryset = ejscreen_subset_geom.objects.all()
    serializer_class = ejscreen_subset_geom_Serializer
    bbox_filter_field = 'geom'
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    fileter_fields = ['id','geoid10','d_ldpnt_2','d_dslpm_2','d_cancr_2','d_resp_2','d_ptraf_2','d_pwdis_2','d_pnpl_2','d_prmp_2','d_ptsdf_2','d_ozone_2','d_pm25_2']
    bbox_filter_include_overlapping = True

class drf_nc_covid_zipcode_geom_View(viewsets.ModelViewSet):
    queryset = nc_covid_zipcode_geom.objects.all()
    serializer_class = nc_covid_zipcode_geom_Serializer
    bbox_filter_field = 'geom'
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    fileter_fields = ['id','zipcode','cases,cases_per_10000_res','cases_per_100000_res','deaths']
    bbox_filter_include_overlapping = True

class drf_ncdot_county_boundaries_View(viewsets.ModelViewSet):
    queryset = ncdot_county_boundaries.objects.all()
    serializer_class = ncdot_county_boundaries_Serializer
    bbox_filter_field = 'geom'
    filter_backends = [DjangoFilterBackend, InBBoxFilter]
    fileter_fields = ['id','objectid','fips','countyname','uppercount','sapcountyi','dotdistric','dotdivisio','sap_cnty_n','cnty_nbr','dstrct_nbr','div_nbr','name','shapestare','shapestlen']
    bbox_filter_include_overlapping = True

