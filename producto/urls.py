path('crud', views.crud, name='crud'),
path('productosAdd', views.productos, name='productosAdd'),

def crud(request):
    productos = productos.objects.all()
    context = {'productos' : productos}
    return render (request, 'producto/productos_list.html', context)

urlpatterns = [
    path('index', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('productosAdd', views.alumnosAdd, name='productosAdd'),

]