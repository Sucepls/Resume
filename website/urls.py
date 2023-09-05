from django.urls import path
from website.views import *

app_name ='website'

urlpatterns = [
    path('', index_view, name='index'),
    path('inner', inner_view, name='inner'),
    path('portfolio', portfolio_view, name='portfolio'),
]