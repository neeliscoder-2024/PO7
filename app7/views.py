from django.shortcuts import render
def html_response(request):
    return render(request,'index.html')
