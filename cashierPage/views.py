from django.shortcuts import render, redirect
from django.views.generic import  ListView, CreateView
from .models import Product, checkOut
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
class index(ListView):
    model = Product
    template_name = 'cshierPage/index.html'
    fields = "__all__"
    
    def get_context_data(self,*args, **kwargs):
        uCashier = checkOut.objects.all()
        context = super().get_context_data(*args,**kwargs)
        context["uCashier"] = uCashier
        return context
    
    
class form(CreateView):
    model = Product
    template_name = 'cshierPage/add_cashier.html'
    fields = "__all__"
    

class new_page(CreateView):
    model = Product
    template_name = 'cshierPage/new_page.html'
    fields = "__all__"
    
    
class add_product(CreateView):
    model = Product
    template_name = 'cshierPage/add_product.html'
    fields = "__all__"
    
    
class regist(CreateView):
    model = Product
    template_name = 'user/register.html'
    fields = "__all__"


class myProfile(CreateView):
    model = Product
    template_name = 'user/page_profile.html'
    fields = "__all__"    
    
def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have been Logged in !!!'))
            return redirect('home')
        else:
            messages.success(request, ('You do not have account yet !!!'))
            return redirect('regist-page')
    else:
        return render(request, 'user/login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged Out !!!'))
    return redirect('home')
    