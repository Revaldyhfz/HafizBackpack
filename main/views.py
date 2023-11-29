import datetime
import json
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.urls import reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    counter = products.count
    if request.method == 'POST':
        if 'increment' in request.POST:
            increment(request, products)
            return HttpResponseRedirect(reverse('main:show_main'))
        elif 'decrement' in request.POST:
            decrement(request, products)
            return HttpResponseRedirect(reverse('main:show_main'))
        elif 'delete' in request.POST:
            delete(request, products)
            return HttpResponseRedirect(reverse('main:show_main'))

    context = {
        'name': request.user.username,
        'class': 'PBP KI', # Your PBP Class
        'products': products,
        'counter' : counter,
        'last_login': request.COOKIES['last_login'],

    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login')
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
@csrf_exempt
def increment(request, products):
    product_id = request.POST.get('increment')
    product = Product.objects.get(id=product_id)
    product.amount += 1
    product.save()

@login_required(login_url='/login')
def decrement(request, products):
    product_id = request.POST.get('decrement')
    product = products.get(id=product_id)
    product.amount -= 1
    product.save()

@login_required(login_url='/login')
def delete(request, products):
    product_id = request.POST.get('delete')
    product = products.get(id=product_id)
    product.delete()

@login_required(login_url='/login')
def edit_product(request, id):
    product = Product.objects.get(pk=id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    else:
        form = ProductForm(instance=product)

    context = {'form': form}
    return render(request, "edit_product.html", context)

@login_required(login_url='/login')
def delete_product(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        fruit_type = request.POST.get("fruit_type")
        user = request.user
        is_discount = request.POST.get("is_discount")

        new_product = Product(name=name, amount=amount, description=description, fruit_type=fruit_type, user=user, is_discount=is_discount)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
@login_required(login_url='/login')
def increment_ajax(request, id):
    item = Product.objects.get(pk=id)
    item.amount += 1
    item.save()
    return JsonResponse({"message": "Quantity incremented successfully"})

@csrf_exempt
def decrement_ajax(request, id):
    item = Product.objects.get(pk=id)
    item.amount -= 1
    item.save()
    return JsonResponse({"message": "Quantity decremented successfully"})

@csrf_exempt
def delete_ajax(request, id):
    item = Product.objects.get(pk=id)
    item.delete()
    return JsonResponse({"message": "Product removed successfully"})


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Product.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"],
            fruit_type = data["fruit_type"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)