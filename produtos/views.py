from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')  # Redireciona para a lista de produtos após adicionar
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar.html', {'form': form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')  # Redireciona para a lista de produtos após editar
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar.html', {'form': form, 'produto': produto})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')  # Redireciona para a lista de produtos após deletar
    return render(request, 'produtos/deletar.html', {'produto': produto})
