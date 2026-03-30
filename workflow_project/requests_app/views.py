from django.shortcuts import render, redirect
from .models import Request

# Create your views here.
def request_list(request):
    requests = Request.objects.all()
    return render(request, 'requests_app/list.html', {'requests': requests})

def create_request(request):
    if request.method == 'POST':
        Request.objects.create(title=request.POST['title'],
         description=request.POST['description'],
         status=request.POST['status']
        )
        return redirect('/')
    return render(request, 'requests_app/create.html')