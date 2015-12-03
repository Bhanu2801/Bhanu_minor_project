from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.shortcuts import render

# Create your views here.
from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap

class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))
@csrf_exempt
def test(request,id):
    return render(request,'map/test1(1).html',{})
@csrf_exempt
def calc(request):
    lat=request.POST.get('lat')
    lon=request.POST.get('lon')
    print lat, lon
    return index(request,lat,lon)

def index(request,lat,lon):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(str(lat),str(lon)),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 12,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    context = {'form': MapForm(initial={'map': gmap})}
    return render(request,'map/index.html', context)