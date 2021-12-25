from django.shortcuts import render
from django.http import HttpResponse, response
from home.models import Product,Category
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    return render(request, 'home/index.html')
def shop(request):
    return render(request, 'home/shop.html')
def products(request):
    listCategory = Category.objects.all();
    products = Product.objects.all()
    return render(request, 'home/products.html',{'catagories':listCategory,'products':products})
def contact(request):
    return render(request, 'home/contact.html')
def checkout(request):
    return render(request, 'home/checkout.html')
def aboutus(request):
    return render(request, 'home/aboutus.html')
def news(request):
    return render(request, 'home/news.html')
def productcat(request,id):
    listCategory = Category.objects.all();
    productCat = Product.objects.filter(cat_id = id)
    return render(request, 'home/productcat.html',{'catagories':listCategory,'productCat':productCat})
def productdetail(request,id):
    listCategory = Category.objects.all()
    detail = Product.objects.get(pro_id = id)
    otherPro = Product.objects.filter(cat_id = detail.cat_id)
    return render(request,'home/productdetail.html',{'catagories':listCategory,'detail':detail,'otherPro':otherPro})
cart = {}
def addcart(request):
    if request.is_ajax():
        id = request.POST.get("id")
        num = request.POST.get("num")
        proDetail = Product.objects.get(pro_id = id)
        if id in cart.keys():
            itemCart = {
                'name':proDetail.pro_name,
                'price':proDetail.pro_price,
                'image':str(proDetail.pro_image),
                'num':int(cart[id]['num'])+1
            }
        else:
            itemCart = {
                'name':proDetail.pro_name,
                'price':proDetail.pro_price,
                'image':str(proDetail.pro_image),
                'num':num
            }
        cart[id] = itemCart
        request.session['cart'] = cart
        cartInfo = request.session['cart']

        html = render_to_string('home/addcart.html',{'cart':cartInfo})
    return HttpResponse(html)

def shoppingcart(request):
    listCategory = Category.objects.all()
    total = 0;
    carts = request.session['cart']
    for key,value in carts.items():
        total +=int(value['price'])*int(value['num'])
    return render(request,'home/shoppingcart.html',{'catagories':listCategory,'total':total})

