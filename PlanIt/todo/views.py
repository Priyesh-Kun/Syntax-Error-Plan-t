from django.shortcuts import render
from login.models import Users
from todo.models import DailyTasks, WeeklyTasks, MonthlyTasks

# Create your views here.

def daily(request):
    # if request.method == "POST":
    return render(request, "Daily_Target.html")