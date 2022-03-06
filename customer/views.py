from django.shortcuts import render,redirect
from django.views.generic import View,DetailView
from  owner.models import Books
from customer.forms import UserRegistrationForm,LoginForm
from  django.contrib.auth import  authenticate,login,logout
# Create your views here.
class CustomerHome(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        context={"books":qs}
        return render(request,"cust_index.html",context)
class SignUpView(View):
    def get(self,request):
        form=UserRegistrationForm()
        context={"form":form}
        return render(request,"signup.html",context)
    def post(self,request):
        form =UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"signup.html")
        else:
            context={"form":form}
            return render(request,"signup.html",context)
class SignInView(View):
 def get(self,request):
     form=LoginForm
     context={"form":form}
     return render(request,"login.html",context)
 def post(self,request):
     form=LoginForm(request.POST)
     if form.is_valid():
         username=form.cleaned_data.get("username")
         password=form.cleaned_data.get("password")
         user=authenticate(username=username,password=password)
         if user:
             login(request,user)
             if request.user.is_superuser:
                 return redirect("listbook")
             else:
                 return redirect("home")
     else:
         context={"form":form}
         return render(request,"login.html",context)

def sign_out(request):
    logout(request)
    return redirect("login")

# class SearchView(View):
#     def get(self,request,*args,**kwargs):
#         book = kwargs['book_name']
#         qs=Books.objects.get(book_name=book)
#         return redirect("bookdetails")
class BookSearch(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "book_details.html"
    pk_url_kwarg = "book_name"