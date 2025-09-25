from django.shortcuts import redirect, render

from lawfirmapp.forms import LawFirmForm
from lawfirmapp.models import LawFirm,AllCases

# Create your views here.
def home(request):
    casedata = AllCases.objects.all()
    return render(request,'lawfirm/home.html',{'casedata':casedata})

def allCases(request):
    casedata = AllCases.objects.all()
    return render(request,'lawfirm/allCases.html',{'casedata':casedata})

def about(request):
    data = LawFirm.objects.last()
    return render(request,'lawfirm/about.html',{'firm':data})

def profile(request):
    form = LawFirmForm()
    if request.method == 'POST':
        form = LawFirmForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("Submitted")
            return redirect('about')
    return render(request,'lawfirm/profile.html',{'form':form})