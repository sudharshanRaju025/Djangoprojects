from django.urls import path
from .views import TicketCreateView,TicketListView, generate_pdf

urlpatterns=[
    path("book/",TicketCreateView.as_view()),
    path("tickets/",TicketListView.as_view(),name="ticket_list"),
    path("tickets/<int:pk>/pdf/", generate_pdf, name="generate_pdf")
]