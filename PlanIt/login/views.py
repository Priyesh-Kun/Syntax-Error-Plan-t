from django.shortcuts import render
from login.models import Users
from django.contrib import messages
import re 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Create your views here.

def index(request):
    return render(request,'index.html')
def sign_up(request):
    login_status = False
    userName = ''
    context={'login_status':login_status, 'userName':userName}
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass_word = request.POST.get('pass_word')
        pass_word_confirm=request.POST.get('pass_word_confirm')
        form = Users.objects.all()
        for data in form:
            if data.user_name == user_name:
                messages.error(request, 'Username already exists. Please enter a different username!!')
                return render(request, "signup.html")
            elif data.email==email:
                messages.error(request, 'Account exists with this email, Please Login Again')
                return render(request, "signup.html")
        if pass_word != pass_word_confirm:
            messages.error(request, 'Both passwords mismatch!!')
            return render(request, "signup.html")
        user = Users(user_name=user_name,name=name,email=email,pass_word=pass_word,pass_word_confirm=pass_word_confirm)
        user.save()

        context['login_status'] = True
        context['userName'] = user_name
        return render(request, 'index.html',context)
    else:
        # login_status = False
        return render(request, 'signup.html')

def login(request):
    login_status = False
    userName = ''
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('pass_word')
        context = {
            'login_status' : login_status,
            'userName' : userName
        }
        form = Users.objects.all()
        context = {'form' : form}
        if re.fullmatch(regex,username):
            for data in form:
                if data.email == username:
                    if data.pass_word == password:
                        context['login_status'] = True
                        context['userName'] = data.user_name
                        messages.success(request,'Successfully Logged In !')
                        return render(request, 'index.html', context)
                    else:
                        login_status = False
                        messages.error(request,'Login Failed, Password entered is incorrect')
                        return render(request, 'signin.html')
                
        else:
            for data in form:
                if data.user_name == username:
                    if data.pass_word == password:
                        context['login_status'] = True
                        context['userName'] = data.user_name
                        messages.success(request,'Successfully Logged In !')
                        return render(request, 'index.html', context)
                    else:
                        login_status = False
                        messages.error(request,'Login Failed, Password entered is incorrect')
                        return render(request, 'signin.html')
               
    return render(request, 'signin.html')

def logout(request):
    login_status = False
    userName = ''
    context = {'login_status' : login_status, 'userName' : userName}
    return render(request,'index.html',context)