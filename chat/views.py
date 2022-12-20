from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, "home.html")

def checkview(request):
  room = request.POST["room_name"]
  username = request.POST["username"]

  pass