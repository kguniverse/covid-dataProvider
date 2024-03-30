from django.urls import path

from . import views

urlpatterns = [
    path("counties", views.get_all_counties, name="counties"),
    path("states", views.get_all_states, name="states"),
    path("statesNested", views.get_states_by_date_and_state, name="statesNested"),
]