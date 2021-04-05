from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView


# class Home(TemplateView):
#     template_name = "home.html"


class Home(ListView):
    template_name = 'home.html'
    context_object_name = 'contact_list'
    
    def get_queryset(self):
        return Contact.objects.all()

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact-detail.html'


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ContactForm()

    return render(request,'create.html',{'form': form})

def edit(request, pk, template_name='edit.html'):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, template_name, {'form':form})


def delete(request, pk, template_name='confirm_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('home')
    return render(request, template_name, {'object':contact})