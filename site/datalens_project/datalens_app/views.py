# datalens_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DatasetForm, DataForm
from .models import Dataset, Data

def index(request):
    # Получаем все датасеты
    datasets = Dataset.objects.all()

    # Фильтрация
    name_contains = request.GET.get('name_contains')
    if name_contains:
        datasets = datasets.filter(name__icontains=name_contains)

    # Сортировка
    sort_by = request.GET.get('sort_by')
    if sort_by == 'name':
        datasets = datasets.order_by('name')
    elif sort_by == 'date_uploaded':
        datasets = datasets.order_by('-date_uploaded')

    # Обработка POST запроса (добавление нового датасета)
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DatasetForm()
    
    return render(request, 'datalens_app/index.html', {'form': form, 'datasets': datasets})

def add_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DataForm()
    return render(request, 'datalens_app/add_data.html', {'form': form})

def create_dataset(request):
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DatasetForm()
    return render(request, 'datalens_app/create_dataset.html', {'form': form})

def dataset_detail(request, dataset_id):
    dataset = get_object_or_404(Dataset, pk=dataset_id)
    return render(request, 'datalens_app/dataset_detail.html', {'dataset': dataset})

def edit_dataset(request, dataset_id):
    dataset = get_object_or_404(Dataset, id=dataset_id)
    if request.method == 'POST':
        form = DatasetForm(request.POST, request.FILES, instance=dataset)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DatasetForm(instance=dataset)
    return render(request, 'datalens_app/edit_dataset.html', {'form': form})

def delete_dataset(request, dataset_id):
    dataset = get_object_or_404(Dataset, id=dataset_id)
    if request.method == 'POST':
        dataset.delete()
        return redirect('index')
    return render(request, 'datalens_app/delete_dataset.html', {'dataset': dataset})