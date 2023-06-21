from django.shortcuts import render
from django.shortcuts import redirect
from django.core.serializers import serialize
from django.utils.html import json_script

from matching.models import User, Requirement, Mission, Skill, Consultant
from matching.forms import UserForm


def connexion(request):
    return render(request, 'matching/connexion.html')


def RM_home(request, id):
    user_connected = User.objects.get(id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user_connected)
        if form.is_valid():
            user_connected = form.save()
    else:
        form = UserForm()
    
    users_random = User.objects.all()
    users_by_name = users_random.order_by('first_name')
    users_by_role = users_random.order_by('role')
    consultants = Consultant.objects.all()

    content = {
        'id': id,
        'user_connected': user_connected,
        'form': form,
        'users_random': users_random,
        'users_by_name': users_by_name,
        'users_by_role': users_by_role,
        'consultants': consultants,
    }
    
    return render(request, 'matching/RM_home.html', content)


def gestion_skills(request):
    return render(request, 'matching/gestion_skills.html')


def gestion_missions(request):
    return render(request, 'matching/gestion_missions.html')
