from django.shortcuts import render, get_object_or_404, redirect
from .models import Author
from .forms import AuthorForm

def author_list(request):
    authors = Author.get_all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'authors/author_detail.html', {'author': author})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'authors/author_form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_detail', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors/author_form.html', {'form': form, 'author': author})
