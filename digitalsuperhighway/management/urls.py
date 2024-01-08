from django.urls import path, include
from management import views
from .views import RecordsViewSets

    
urlpatterns = [   
    path('all-records/', RecordsViewSets.as_view({'get': 'records_list'}), name='all-records'),
    path('create-record/', RecordsViewSets.as_view({'post': 'create_record'}), name='create-record'),
    path('publicwifi-count/', RecordsViewSets.as_view({'get': 'get_publicwifi_count'}), name='publicwifi-count'),
    path('publicwifi/', RecordsViewSets.as_view({'get': 'get_publicwifi'}), name='publicwifi'),
    path('lastmile/', RecordsViewSets.as_view({'get': 'get_lastmile'}), name='lastmile'),
    path('lastmile-count/', RecordsViewSets.as_view({'get': 'get_lastmile_count'}), name='lastmile-count'),
    path('update-record/<str:pk>/', RecordsViewSets.as_view({'patch': 'update_record'}), name='update-record'),
]