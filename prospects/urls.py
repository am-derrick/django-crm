from django.urls import path
from prospects.views import prospect_list, prospect_detail

app_name = 'prospects'

urlpatterns = [
    path('', prospect_list),
    path('<pk>', prospect_detail)
]
