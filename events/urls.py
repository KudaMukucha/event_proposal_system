from django.urls import path
from . import views

urlpatterns =[
    path('create-event-proposal/',views.create_event_proposal,name='create-event-proposal'),
    path('all-event-proposals/',views.all_event_proposals,name='all-event-proposals'),
    path('event-proposal-queue/',views.event_proposal_queue,name='event-proposal-queue'),
    path('admin-response/<int:pk>/',views.admin_response,name='admin-response')
    
]


