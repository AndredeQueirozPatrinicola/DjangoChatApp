from django.shortcuts import redirect, render
from django.contrib.auth import login 

from .forms import SignUpForm


# Create your views here.


def landingpage(request):
    return render(request, 'landingpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('landingpage')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})