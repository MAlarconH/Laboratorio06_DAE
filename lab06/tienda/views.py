from django.shortcuts import get_object_or_404, render

from .models import Producto, Categoria

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    category_list = Categoria.objects.order_by('nombre')
    context = {'product_list': product_list, 'category_list':category_list}
    return render(request, 'index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    category_list = Categoria.objects.order_by('nombre')
    return render(request, 'producto.html', {'producto':producto, 'category_list':category_list})

def categoria(request, categoria_id):
    productos = Producto.objects.filter(categoria=categoria_id)
    category_list = Categoria.objects.order_by('nombre')
    return render(request, 'categoria.html', {'productos':productos, 'category_list':category_list})
    
