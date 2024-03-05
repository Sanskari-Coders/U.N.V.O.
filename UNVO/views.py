from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from UNVOmessagebox.models import Messages

def index(request):
    context={'context':Messages.objects.all()}
    return render(request,'index.html',context)


@csrf_exempt
def messageinput(request):
    if request.method == 'POST':
        msg = request.POST.get('messagesent')
        if msg :
            nemg=Messages(message=msg)
            nemg.save()
        return redirect('home')
    return render(request, 'index.html')
    