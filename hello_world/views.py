from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    print("Hello LR H K!")
    


    """ 

    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)
   
    """