from django.shortcuts import render

# Create your views here.
def store(request):
    return render(request,'store/store.html')
def profile(request):
    return render(request,'store/profile.html')
def logout(request):
    return render(request,'store/logout.html')
