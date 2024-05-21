import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Record, Cart, CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import OrderForm


def record_list(request):
    query = request.GET.get('q')
    if query:
        records_list = Record.objects.filter(
            Q(artist__icontains=query) |
            Q(album_name__icontains=query) |
            Q(release_year__icontains=query) |
            Q(price__icontains=query) |
            Q(genres__icontains=query)
        )
    else:
        records_list = Record.objects.all().order_by('?')

    paginator = Paginator(records_list, 10)

    page = request.GET.get('page')
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    return render(request, 'records/record_list.html', {'records': records})

def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'records/record_detail.html', {'record': record})

def add_to_cart(request, record_id):
    cart, created = Cart.objects.get_or_create(id=request.session.get('cart_id'))
    if created:
        request.session['cart_id'] = cart.id
    record = get_object_or_404(Record, id=record_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, record=record)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    cart = get_object_or_404(Cart, id=request.session.get('cart_id'))
    form = OrderForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Обработка данных формы и создание заказа
        card_number = form.cleaned_data['card_number']
        cvv = form.cleaned_data['cvv']
        
        # Сохранение данных заказа в файл (в целях демонстрации)
        with open('order.txt', 'a') as f:
            f.write(f'Card Number: {card_number}, CVV: {cvv}\n')
        
        # Очистка корзины после успешного оформления заказа
        cart.cartitem_set.all().delete()
        return redirect('success_page')  # Перенаправление на страницу успешного оформления заказа
        
    return render(request, 'records/cart_detail.html', {'cart': cart, 'form': form})

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart_detail')

def upload_image(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.method == 'POST':
        record.image = request.FILES.get('image')
        record.save()
        return redirect('record_detail', pk=record_id)
    return render(request, 'records/upload_image.html', {'record': record})

def success_page(request):
    return render(request, 'records/success_page.html')