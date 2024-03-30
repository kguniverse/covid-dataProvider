from django.http import HttpResponse
from django.core import serializers
from .models import Counties, States
import json

state_by_date = {}
initial_state = False

def lazy_init():
    states = States.objects.values()
    states_name = States.objects.values('state').distinct()
    states_name_fips = []
    for state in states_name:
        fips = States.objects.filter(state=state['state']).values('fips').distinct()
        states_name_fips.append({
            'state': state['state'],
            'fips': fips[0]['fips']
        })
    for state in states:
        date_key = state['date'].strftime('%Y-%m-%d')
        if date_key not in state_by_date:
                state_by_date[date_key] = {}
        state['date'] = state['date'].strftime('%Y-%m-%d')
        state_by_date[date_key][int(state['fips'])] = state
    
    for date in state_by_date:
        for state in states_name_fips:
            if int(state['fips']) not in state_by_date[date]:
                state_by_date[date][int(state['fips'])] = {
                    'date': date,
                    'state': state['state'],
                    'fips': state['fips'],
                    'cases': 0,
                    'deaths': 0
                }

    initial_state = True


def get_all_counties(request):
    counties = Counties.objects.values()
    for county in counties:
        county['date'] = county['date'].strftime('%Y-%m-%d')
    return HttpResponse(json.dumps(list(counties)), content_type='application/json')

def get_all_states(request):
    states = States.objects.values()
    for state in states:
        state['date'] = state['date'].strftime('%Y-%m-%d')
    return HttpResponse(json.dumps(list(states)), content_type='application/json')

def get_states_by_date_range(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    states = States.objects.filter(date__range=[start_date, end_date]).values()
    for state in states:
        state['date'] = state['date'].strftime('%Y-%m-%d')
    return HttpResponse(json.dumps(list(states)), content_type='application/json')

def get_counties_by_date_range(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    counties = Counties.objects.filter(date__range=[start_date, end_date]).values()
    for county in counties:
        county['date'] = county['date'].strftime('%Y-%m-%d')
    return HttpResponse(json.dumps(list(counties)), content_type='application/json')

# allow for zero cases
def get_states_by_date_and_state(request):
    if initial_state == False:
        lazy_init()
    return HttpResponse(json.dumps(state_by_date), content_type='application/json')
