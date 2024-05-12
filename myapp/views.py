from django.shortcuts import render, get_object_or_404
from .models import Client, Order, Product
from datetime import timedelta, datetime
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm


def index(request):
    return render(request, 'myapp/index.html')


def week(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    today = datetime.now()
    last_week_start = today - timedelta(days=today.weekday())
    last_week_end = last_week_start + timedelta(days=6)
    orders = Order.objects.filter(
        client=client,
        order_date__gte=last_week_start,
        order_date__lte=last_week_end
    ).order_by('-order_date')
    return render(request, 'myapp/week.html', {"client": client, "orders": orders})


def month(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    today = datetime.now()
    last_30_days_start = today - timedelta(days=30)
    orders = Order.objects.filter(
        client=client,
        order_date__gte=last_30_days_start,
        order_date__lte=today
    ).order_by('-order_date')
    return render(request, 'myapp/week.html', {"client": client, "orders": orders})


def year(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    today = datetime.now()
    last_year_start = today - timedelta(days=365)
    orders = Order.objects.filter(
        client=client,
        order_date__gte=last_year_start,
        order_date__lte=today
    ).order_by('-order_date')
    return render(request, 'myapp/week.html', {"client": client, "orders": orders})


def upload_image(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            product.image = image
            product.save()
    else:
        form = ImageForm()
    return render(request, 'myapp/upload_image.html', {'form': form})
