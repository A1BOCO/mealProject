from django.contrib.auth import authenticate, login

from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm

def loginuser(request):

    if request.method == "POST":
        #username = request.POST['username']
        #password = request.POST['password']
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,user=username, password=password)
        if user is not None:
            login(request,user)
    login_form = AuthenticationForm()

    return {'loginform':login_form }