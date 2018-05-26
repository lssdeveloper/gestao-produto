from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto
from .forms import ProdutoForm


@login_required
def prod_lista(request):
    produtos = Produto.objects.all()
    return render(request, 'prod_lista.html', {'produtos': produtos})


@login_required
def prod_novo(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('prod_lista')
    return render(request, 'prod_form.html', {'form': form})


@login_required
def prod_update(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('prod_lista')

    return render(request, 'prod_form.html', {'form': form})


@login_required
def prod_delete(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('prod_lista')

    return render(request, 'prod_delete_confirm.html', {'produto': produto})


"""
def my_logout(request):
    logout(request)
    return redirect('home')
"""
