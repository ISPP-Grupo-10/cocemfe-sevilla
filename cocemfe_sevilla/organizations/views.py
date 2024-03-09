from django.shortcuts import render, redirect, get_object_or_404
from .models import Organization
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import OrganizationForm
from professionals.views import is_admin

@user_passes_test(is_admin)
def create_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizations:organization_list')  
    else:
        form = OrganizationForm()
    return render(request, 'create_organization.html', {'form': form})

@user_passes_test(is_admin)
def organization_options(request):
    return render(request, 'organization_options.html')

@user_passes_test(is_admin)
def get_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    return render(request, 'organization_detail.html', {'organization': organization})

@user_passes_test(is_admin)
def update_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('organizations:organization_list') 
    else:
        form = OrganizationForm(instance=organization)
    return render(request, 'update_organization.html', {'form': form})

@user_passes_test(is_admin)
def delete_organization(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    organization.delete()
    return redirect('organizations:organization_list')

@user_passes_test(is_admin)
def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organizations_list.html', {'organizations': organizations})