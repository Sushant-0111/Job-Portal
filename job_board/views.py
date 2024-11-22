from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Job

# Create your views here.


def index(request):
    active_posting = Job.objects.filter(is_active=True)
    context = {
        'job_posting': active_posting,
    } 
    return render(request, 'job_board/index.html', context)


def job_details(request , pk):
    job_detail = get_object_or_404(Job, pk=pk , is_active=True) 
    context= {
        'job_detail': job_detail
    }
    return render(request , 'job_board/details.html',context)