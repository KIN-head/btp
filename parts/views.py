from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Order, Category, Product, OrderItem
import openpyxl
from cart.forms import CartAddProductForm
from cart.cart import Cart
from .forms import OrderCreateForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def orders_list(request):
    #return render(request, 'parts/request_list.html', {})
    orders = Order.objects.filter(updated__lte=timezone.now()).order_by('updated')
    return render(request, 'parts/orders_list.html', {'Orders': orders})

def index(request):
    return render(request, 'parts/index.html', {})

def order_new(request):
    return render(request, 'parts/order_new.html', {})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'parts/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'parts/product/detail.html',
                  {'product': product})

@login_required(login_url='/account/login/')
def order_from_file(request):
    if "GET" == request.method:
        return render(request, 'parts/order_from_file.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        ws = wb.active
        #print(ws)

        excel_data = list()
        #ordr = Order.objects.Create(owner=self.request.user.usermane)
        # iterating over the rows and
        # getting value from each cell in row
        cart = Cart(request)
        for row in ws.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            pdct = Product.objects.get_or_create(name=row_data[0])
            prod = get_object_or_404(Product, name=row_data[0])
            #quantity = int(row_data[1])
            #order_items =
            if  pdct:
                #excel_data.append(str(prod.id))
                #cart.add(prod)
                cart.add(product=prod, quantity=int(row_data[1]),
                         update_quantity='update')
            excel_data.append(row_data)

    return redirect('cart_detail')
    #return render(request, 'cart/detail.html', {'cart': cart})
    #return render(request, 'parts/order_from_file.html', {"excel_data":excel_data})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'parts/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'parts/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'parts/order/create.html',
                  {'cart': cart, 'form': form})
