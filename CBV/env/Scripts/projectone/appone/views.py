from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Ticket
from .forms import TicketForm,SearchForm

def search_view(request,CreateView):
     form=SearchForm(request.GET or None)
     results=[]
     if form.is_valid():
          query=form.cleaned_data.get("query")
          results=Ticket.objects.filter(user_name__icontains="nameone")
     return render(request,"search_results.html",{"form":form,"results":results})

class TicketCreateView(CreateView):

    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_form.html'
    success_url = reverse_lazy('ticket_list')

class TicketListView(ListView):

     model = Ticket
     template_name = 'ticket_list.html'


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

def generate_pdf(request, pk):
     
     ticket = Ticket.objects.get(pk=pk)
     html = render_to_string('ticket_pdf.html', {'ticket': ticket})
     response = HttpResponse(content_type="application/pdf")
     response['Content-Disposition'] = f'attachment; filename="ticket_{ticket.id}.pdf"'
     weasyprint.HTML(string=html).write_pdf(response)
     return response


def ticket_pdf_view(request, ticket_id):
     ticket = get_object_or_404(Ticket, id="ticket_id")
     context = {'ticket' : ticket}
     return render(request, 'ticket_pdf.html'. context)