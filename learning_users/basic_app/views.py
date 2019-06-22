from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm, MicroPostForm
from basic_app.models import MicroPost
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 'basic_app/registration.html', 
                            {'user_form': user_form,
                            'profile_form': profile_form,
                            'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        
        else:
            print('Someone tried to login and failed!')
            print('Username: {} and password {}'.format(username, password))
            return HttpResponse("invalid login details supplied!")
    
    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def create_post(request):

    posted = False

    if request.method == 'POST':
        micropost_form = MicroPostForm(data=request.POST)
        if micropost_form.is_valid():
            micropost = micropost_form.save(commit=False)
            micropost.pub_date = timezone.now()
            micropost.user = request.user
            micropost.save()
            posted = True
            print("saved{}".format(micropost.content))
            return redirect('basic_app:show_post')
        else:
            print(micropost_form.errors)
    else:
        micropost_form = MicroPostForm()

    return render(request, 'basic_app/micropost.html', {'micropost_form': micropost_form,
                                                        'posted': posted})

def show_post(request):
    microposts = MicroPost.objects.order_by('pub_date')
    return render(request, 'basic_app/posts.html', {'microposts': microposts})

def delete_post(request, pk):
    post = get_object_or_404(MicroPost, pk=pk)
    post.delete()
    return redirect('basic_app:show_post')

@login_required
def edit_post(request, pk):

    old_post = get_object_or_404(MicroPost, pk=pk)

    if request.method == 'POST':
        micropost_form = MicroPostForm(data=request.POST,instance=old_post)
        if micropost_form.is_valid():
            micropost = micropost_form.save(commit=False)
            micropost.pub_date = timezone.now()
            micropost.user = request.user
            micropost.save()
            return redirect('basic_app:show_post')
        else:
            print(micropost_form.errors)
    else:
        micropost_form = MicroPostForm(instance=old_post)

    return render(request, 'basic_app/post_edit.html', {'micropost_form': micropost_form})