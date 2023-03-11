from django.shortcuts import (render,
                              redirect)
from django.contrib.auth import (authenticate,
                                 login)
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import (SignUpForm)

def login(request):
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'layout.html')

def signup(request):

	if request.method == 'POST':

		sign_up_form = SignUpForm(request.POST)

		if sign_up_form.is_valid():

			sign_up_form.cleaned_data['first_name'] = f'''{sign_up_form.cleaned_data['first_name']}'''.upper()
			sign_up_form.cleaned_data['last_name'] = f'''{sign_up_form.cleaned_data['last_name']}'''.upper()

			sign_up_form.save()
			
			return redirect('home')
	else:

		sign_up_form = SignUpForm()

	context = { 'sign_up_form' : sign_up_form }

	return render(request, 'signup.html', context)
