from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    name='pragati'
    OnlineVotingSystem ={
        "VotingBooth1":{
            "name":"pragati",


        }
    }
    context = {"display_name":name, "OnlineVotingSystem":"OnlineVotingSyste"}
    return render(request,"home.html",context)