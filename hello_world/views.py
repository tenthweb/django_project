from django.shortcuts import render

from django.http import HttpResponse

def index(request):

    return HttpResponse("Hello LR H K!")
    


    """ 

    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)
   
    """