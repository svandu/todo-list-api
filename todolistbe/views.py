from django.http import HttpResponse

def homePage(request): 
    print("home page requested")
    return HttpResponse("this is home page")
    