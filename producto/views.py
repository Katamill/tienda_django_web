from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def contacto(request):
    return render(request, 'pages/contacto.html')

def envios(request):
    return render(request, 'pages/envios.html')

def nosotros(request):
    return render(request, 'pages/nosotros.html')

def tienda(request):
    return render(request, 'pages/tienda.html')

def carrito(request):
    return render(request, 'pages/carrito.html')

def admini(request):
    return render(request, 'pages/admini.html')




def productosAdd(request):
    if request.method is not "POST":
        productos = Producto.objects.all()
        context = {'productos': productos}
        return render(request, 'producto/productos_add.html', context)
   


