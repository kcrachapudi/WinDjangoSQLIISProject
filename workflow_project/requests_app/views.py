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

from django.shortcuts import render, redirect, get_object_or_404
from .models import Request

# List all requests
def request_list(request):
    requests = Request.objects.all()
    return render(request, 'requests_app/list.html', {'requests': requests})

# Create new request
def request_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        Request.objects.create(title=title, description=description, status=status)
        return redirect('request_list')
    return render(request, 'requests_app/create.html')

# Edit request
def request_edit(request, pk):
    req = get_object_or_404(Request, pk=pk)
    if request.method == 'POST':
        req.title = request.POST['title']
        req.description = request.POST['description']
        req.status = request.POST['status']
        req.save()
        return redirect('request_list')
    return render(request, 'requests_app/edit.html', {'request_obj': req})

# Delete request
def request_delete(request, pk):
    req = get_object_or_404(Request, pk=pk)
    if request.method == 'POST':
        req.delete()
        return redirect('request_list')
    return render(request, 'requests_app/delete.html', {'request_obj': req})