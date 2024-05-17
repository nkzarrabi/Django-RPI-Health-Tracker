# inventory/views.py


from django.shortcuts import render, get_object_or_404, redirect
from .models import Rug, Photo
from .forms import RugForm, PhotoForm, SearchForm
from django.forms import modelformset_factory
from django.db.models import Q

def rug_list(request):
    rugs = Rug.objects.all()
    return render(request, 'inventory/rug_list.html', {'rugs': rugs})

def rug_detail(request, pk):
    rug = get_object_or_404(Rug, pk=pk)
    photos = rug.photos.all()
    return render(request, 'inventory/rug_detail.html', {'rug': rug, 'photos': photos})

def rug_new(request):
    PhotoFormSet = modelformset_factory(Photo, form=PhotoForm, extra=3)
    if request.method == "POST":
        form = RugForm(request.POST)
        formset = PhotoFormSet(request.POST, request.FILES, queryset=Photo.objects.none())
        if form.is_valid() and formset.is_valid():
            rug = form.save()
            for form in formset.cleaned_data:
                if form:
                    photo = form['image']
                    photo_instance = Photo(rug=rug, image=photo)
                    photo_instance.save()
            return redirect('rug_detail', pk=rug.pk)
    else:
        form = RugForm()
        formset = PhotoFormSet(queryset=Photo.objects.none())
    return render(request, 'inventory/rug_form.html', {'form': form, 'formset': formset})

def rug_edit(request, pk):
    rug = get_object_or_404(Rug, pk=pk)
    PhotoFormSet = modelformset_factory(Photo, form=PhotoForm, extra=3)
    if request.method == "POST":
        form = RugForm(request.POST, instance=rug)
        formset = PhotoFormSet(request.POST, request.FILES, queryset=Photo.objects.filter(rug=rug))
        if form.is_valid() and formset.is_valid():
            form.save()
            for form in formset.cleaned_data:
                if form:
                    photo = form['image']
                    photo_instance = Photo(rug=rug, image=photo)
                    photo_instance.save()
            return redirect('rug_detail', pk=rug.pk)
    else:
        form = RugForm(instance=rug)
        formset = PhotoFormSet(queryset=Photo.objects.filter(rug=rug))
    return render(request, 'inventory/rug_form.html', {'form': form, 'formset': formset})

def rug_delete(request, pk):
    rug = get_object_or_404(Rug, pk=pk)
    rug.delete()
    return redirect('rug_list')

def home(request):
    return render(request, 'inventory/home.html')

def search(request):
    form = SearchForm()
    results = []
    query = ''
    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            sku = form.cleaned_data['sku']
            size = form.cleaned_data['size']
            age = form.cleaned_data['age']
            country_of_origin = form.cleaned_data['country_of_origin']
            texture = form.cleaned_data['texture']
            style = form.cleaned_data['style']
            color = form.cleaned_data['color']

            filters = Q()
            if query:
                filters &= Q(name__icontains=query) | Q(description__icontains=query)
            if sku:
                filters &= Q(sku__icontains=sku)
            if size:
                filters &= Q(size__icontains=size)
            if age:
                filters &= Q(age=age)
            if country_of_origin:
                filters &= Q(country_of_origin__icontains=country_of_origin)
            if texture:
                filters &= Q(texture=texture)
            if style:
                filters &= Q(style=style)
            if color:
                filters &= Q(color__icontains=color)

            results = Rug.objects.filter(filters)
    return render(request, 'inventory/search.html', {'form': form, 'results': results, 'query': query})