from django.shortcuts import render, HttpResponse
from myapp.models import Training
from myapp.models import Job


def first(request):
    return render(request, 'first.html')

def trainings(request):
    first=Training.objects.all()
    return render(request, 'trainings.html', {'trainings': first})

   

def jobs(request):
    second=Job.objects.all()
    return render(request,'jobs.html',{
        'jobs':second
    })



def  profile(request):
    return render(request,'profile')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")  # 'worker' or 'employer'

        if not username or not password or not role:
            messages.error(request, "All fields are required.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, role=role)
        messages.success(request, "Account created! Please login.")
        return redirect('login')

    return render(request, "signup.html")

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")  # 'worker' or 'employer'

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if hasattr(user, 'userprofile') and user.userprofile.role == role:
                login(request, user)
                if role == "worker":
                    return redirect('worker_dashboard')  # worker dashboard
                else:
                    return redirect('employer_dashboard')  # employer dashboard
            else:
                messages.error(request, "Role mismatch. Please choose the correct role.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")



def user_logout(request):
    return render(request,'logout.html')




def worker_dashboard(request):
    return render(request,'worker.html')




















from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WorkerProfile

@login_required
def worker_profile_settings(request):
    profile = request.user.workerprofile

    if request.method == "POST":
        # User basic info
        request.user.first_name = request.POST.get("first_name")
        request.user.last_name = request.POST.get("last_name")
        request.user.email = request.POST.get("email")
        request.user.save()

        # Worker profile info
        profile.phone = request.POST.get("phone")
        profile.location = request.POST.get("location")
        profile.skills = request.POST.get("skills")
        profile.experience = request.POST.get("experience")
        profile.bio = request.POST.get("bio")
        profile.save()

        messages.success(request, "Profile updated successfully!")

    return render(request, "worker_profile_settings.html", {"profile": profile})
