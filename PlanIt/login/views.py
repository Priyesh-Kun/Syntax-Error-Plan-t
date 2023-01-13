from django.shortcuts import render
from login.models import Users
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass_word = request.POST.get('pass_word')
        user = Users(user_name=user_name,name=name,email=email,pass_word=pass_word)
        user.save()
        return render(request, 'index.html')
    return render(request, 'signup.html')

def login(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pass_work')
    form = Users.objects.all()
    context = {'form' : form}
    for data in form:
        if data.user_name == username:
            if data.pass_word == password:
                return render(request, 'index.html')
            else:
                return render(request, 'login.html')
        else:
            return render(request,'login.html') 