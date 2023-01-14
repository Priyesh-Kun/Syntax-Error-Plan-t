from django.shortcuts import render
from login.models import Users
from todo.models import DailyTasks, WeeklyTasks, MonthlyTasks

# Create your views here.

def daily(request):
    # if request.method == "POST":
    return render(request, "Daily_Target.html")

def monthly(request):
    # if request.method == "POST":
    return render(request, "monthly_target.html")

def weekly(request):
    # if request.method == "POST":
    return render(request, "weekly_target.html")