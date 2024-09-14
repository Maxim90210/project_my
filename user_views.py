from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User created successfully'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = UserCreationForm()
        return render(request, 'users/registerrr.html', {'form': form})

def user_list(request):
    users = CustomUser.objects.all()
    data = [{"username": user.username, "phone_number": user.phone_number} for user in users]
    return JsonResponse(data, safe=False)
