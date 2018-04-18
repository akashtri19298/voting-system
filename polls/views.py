from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import VoterDetails, Candidate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'polls/index.html')


def login(request):
    return render(request, 'polls/login_page.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            voter=form.save()
            user = User.objects.create_user(voter.voter_username, voter.voter_email,voter.voter_password)
            user.first_name=voter.voter_name
            user.save()
            voter.delete()
            v=VoterDetails(voter_user=user,voter_roll=voter.voter_roll)
            v.save()
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'polls/register.html', {'form': form})

@login_required
def vote(request):
    k=request.POST.get('choice')
    if k:
        c = Candidate.objects.get(pk=request.POST.get('choice'))
        c.vote_count+=1
        c.save()
        cur_user=request.user
        print("name=",request.user.first_name)
    
    return render(request,'polls/vote.html',context={'candidate':Candidate.objects.all(),'current_user':request.user})
    


def results(request):
    max=0  
    candidate=Candidate.objects.all()
    for c in candidate:
        print(c,c.id,c.vote_count)
        if c.vote_count>max:
            max=c.vote_count
            i=c.id
                    
    return render(request, 'polls/results.html',context={'winner':Candidate.objects.get(id=i)})