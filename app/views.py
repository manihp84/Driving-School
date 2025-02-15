from django.shortcuts import render , HttpResponse
from .models import Instructor, Booking,Payment
# Create your views here.


def home(request):
    a=Instructor.objects.all()
    return render(request,'base.html',{'a':a})