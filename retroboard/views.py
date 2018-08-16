from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Board, Positive, Delta, ActionItem

# Create your views here.
def index(request):
	latest = Board.objects.latest('id')
	if not latest.is_started:
		return render(request, "retroboard/soon.html")
	context = {
		'positives': latest.positive_set.all(),
		'deltas': latest.delta_set.all(),
		'actions': latest.actionitem_set.all()
	}	
	return render(request, 'retroboard/home.html', context)

def export_view(request):
	latest = Board.objects.latest('id')
	sprint = latest.sprint
	positives = latest.positive_set.all()
	deltas = latest.delta_set.all()
	actions = latest.actionitem_set.all()

	content = sprint
	content += "\n"
	content += "Positives:"
	content += "\n"
	for positive in positives:
		if positive.user:
			content += str(positive.user)
			content += ": "
		content += positive.note
		content += "\n"
	

	content += "\n"
	content += "Deltas:"
	content += "\n"
	for delta in deltas:
		if delta.user:
			content += str(delta.user)
			content += ": "
		content += delta.note
		content += "\n"
	
	content += "\n"
	content += "Action Items:"
	content += "\n"
	for action in actions:
		if action.user:
			content += str(action.user)
			content += ": "
		content += action.note
		content += "\n"
	return HttpResponse(content, content_type='text/plain')

def actions_view(request):
	context = {
		'incomplete': ActionItem.objects.all().filter(is_completed=False),
		'complete': ActionItem.objects.all().filter(is_completed=True)
	}
	return render(request, 'retroboard/actions.html', context)
	
def complete_view(request):
	if request.method == 'POST':
		action_id = request.POST["id"]
		item = ActionItem.objects.get(id=action_id)
		if item is not None:
			item.is_completed = True
			item.save()
			return JsonResponse({"success": True})
		return JsonResponse({"success": False})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("login"))

    else:
        form = UserCreationForm()

    return render(request, 'retroboard/index.html', {'form': form})

def login_view(request):
	if request.method == 'GET':
		return render(request, "retroboard/login.html")

	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "retroboard/login.html", {"message": "Invalid credentials."})

def logout_view(request):
	logout(request)
	return render(request, "retroboard/login.html", {"message": "Logged out."})

def submit_view(request):
	if request.method == 'GET':
		return render(request, "retroboard/submit.html", {"is_authenticated": request.user.is_authenticated})

	note = request.POST["note"]

	latest = Board.objects.latest('id')	


	user = request.user

	if "anon" in request.POST or not request.user.is_authenticated:
		user = None

	sticky_type = request.POST["type"]	
	if sticky_type == 'positive':
		positive = Positive.objects.create(parent_board=latest, user=user, note=note)
		positive.save()
	elif sticky_type == 'delta':
		delta = Delta.objects.create(parent_board=latest, user=user, note=note)
		delta.save()
	elif sticky_type =='action':
		action = ActionItem.objects.create(parent_board=latest, user=user, note=note)
		action.save()

	return HttpResponseRedirect(reverse("submit"))


