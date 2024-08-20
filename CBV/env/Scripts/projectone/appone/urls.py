from django.urls import path
from .views import TicketCreateView,TicketListView, generate_pdf,search_view

urlpatterns=[
    path("book/",TicketCreateView.as_view()),
    path("tickets/",TicketListView.as_view(),name="ticket_list"),
    path("tickets/<int:pk>/pdf/", generate_pdf, name="generate_pdf"),
    path("search/",search_view,name'search_view')
]