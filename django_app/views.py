from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout


from .forms import CreateUser
from django.contrib import messages


# Create your views here.
def HomePage(request):
    context = {}
    return render(request, "app.html", context)

# def RegisterPage(request):
#     context = {}
#     return render(request, "accounts/register.html", context)

def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        form = CreateUser()

        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                messages.success(request, "Account has been created for " + user)
                return redirect('login')
    context = {'form': form}
    return render(request, "accounts/register.html", context)


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('/')


    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                # username  + " is not valid"
                f = f"{username} does not exist... PLease create an account or Enter correct pins"
                messages.info(request, f)

    # form = UserCreationForm()

    context = {}
    return render(request, "accounts/login.html", context)
            

def LogoutPage(request):
    logout(request)
    return redirect('login')