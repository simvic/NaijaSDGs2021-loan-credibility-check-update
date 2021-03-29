from django.shortcuts import render

# Create your views here.
def loan(request):
    context = {}
    return render(request, 'pages/loan-check.html',  context)