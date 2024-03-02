from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, DetailView, UpdateView

from .models import Professional
from .forms import ProfessionalForm


class EditUserView(View):
    def get(self, request, pk):
        professional = get_object_or_404(Professional, id=pk)
        form = ProfessionalForm(instance=professional)
        return render(request, 'professional_detail.html', {'form': form, 'professional': professional})

    def professional_update_view(request, pk):
        professional = get_object_or_404(Professional, pk=pk)

    def post(self, request, pk):
        professional = get_object_or_404(Professional, id=pk)
        form = ProfessionalForm(request.POST, instance=professional)
        if form.is_valid():
            form.save()
            return redirect('/?message=Profesional editado&status=Success')
        else:
            return render(request, 'professional_detail.html', {'form': form, 'professional': professional})


def professional_list(request):
    professionals = Professional.objects.all()
    name_filter = request.GET.get('name', '')
    if name_filter:
        professionals = professionals.filter(name__icontains=name_filter)

    return render(request, 'professional_list.html', {'professionals': professionals})


def delete_professional(request, id):
    professional = get_object_or_404(Professional, id=id)
    print(professional)

    if request.method == 'POST':
        professional.delete()

    professionals = Professional.objects.all()

    return render(request, 'professional_list.html', {'professionals': professionals})

