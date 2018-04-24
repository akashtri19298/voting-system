from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import VoterDetails, Candidate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'polls/index.html',context={'current_user':request.user})


def login(request):
    return render(request, 'polls/login_page.html',context={'current_user':request.user})

def reg_successful(request):
    return render(request,'polls/reg_successful.html',context={'current_user':request.user})

def invalid_vote(request):
    return render(request,'polls/invalid_vote.html',context={'current_user':request.user})


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
            return redirect('reg_successful')
    else:
        form = RegisterForm()
    return render(request, 'polls/register.html',context={'current_user':request.user,'form':form})

@login_required
def vote(request):
    k=request.POST.get('choice')
    cur_user=request.user
    if k:
        c = Candidate.objects.get(pk=request.POST.get('choice'))
        if cur_user.voterdetails.candidate_voted:
            return redirect('invalid_vote')
        c.vote_count+=1
        c.save()
        cur_user.voterdetails.candidate_voted=c
        #print(candidate.profile_image)
        cur_user.voterdetails.save()
                    
    return render(request,'polls/vote.html',context={'candidate':Candidate.objects.all(),'current_user':request.user})
    


def results(request):
    max=0  
    candidate=Candidate.objects.all()
    for c in candidate:
        print(c,c.id,c.vote_count)
        if c.vote_count>max:
            max=c.vote_count
            i=c.id
                    
    return render(request, 'polls/results.html',context={'clist':list(Candidate.objects.order_by("-vote_count")),'current_user':request.user})