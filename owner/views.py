from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,CreateView,DeleteView,UpdateView
from owner.models import Books
from  owner.forms import BookForm
from  django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


# Create your views here.
class BookList(ListView):
    model = Books
    context_object_name = "books"
    template_name = "book_list.html"

class AddBook(CreateView):
    model = Books
    form_class = BookForm
    template_name = "book_add.html"
    success_url =reverse_lazy("listbook")


class BookDetails(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "book_details.html"
    pk_url_kwarg = "id"



class BookDelete(DeleteView):
    def get(self, request, *args, **kwargs):
        id=kwargs['id']
        book=Books.objects.get(id=id)
        book.delete()
        return redirect("listbook")

def sign_out(request):
    logout(request)
    return redirect("login")

class BookUpdate(UpdateView):
    model = Books
    template_name = "book_edit.html"
    form_class = BookForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")