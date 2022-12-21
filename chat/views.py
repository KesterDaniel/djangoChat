from django.shortcuts import render, redirect
from .models import Room, Message

# Create your views here.

def home(request):
  return render(request, "home.html")

def room(request, room):
  username = request.GET.get("username")
  room_details = Room.objects.get(name=room)
  return render(request, "room.html", {"room_details": room_details, "room": room, "username": username})

def checkview(request):
  room = request.POST["room_name"]
  username = request.POST["username"]

  if Room.objects.filter(name=room).exists():
    return redirect("/" + room + "/?username=" + username)
  else:
    new_room = Room.objects.create(name=room)
    new_room.save()
    return redirect("/" + room + "/?username=" + username)