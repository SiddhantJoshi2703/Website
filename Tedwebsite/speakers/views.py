from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .forms import SpeakerModelForm
from django.contrib import messages
from blog.models import Post

def speakers_home(request):
    return render(request, 'speakers/speakers.html')


def addSpeaker(request):
    if request.method == 'POST':
        form = SpeakerModelForm(request.POST)
        if form.is_valid():
            form.save()
    form = SpeakerModelForm()
    return render(request, 'speakers/form.html', {'form': form})


def nominate_yourself(request):
    return render(request, 'speakers/form2.html')

def nominate_others(request):
    return render(request, 'speakers/speakers.html')


def unrestricted(request):
    return render(request, 'speakers/unrestricted.html')

def blogs(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/blog.html',{'posts': posts})

def about_us(request):
    return render(request, 'about_us/about_us.html')

def contact(request):
    return render(request, 'speakers/contact.html')


def speakerDesc1(request):
    return render(request, 'speakers/speaker21.html')


def speakerDesc2(request):
    return render(request, 'speakers/speaker22.html')


def speakerDesc3(request):
    return render(request, 'speakers/speaker23.html')


def speakerDesc4(request):
    return render(request, 'speakers/speaker24.html')


def speakerDesc5(request):
    return render(request, 'speakers/speaker25.html')


def speakerDesc6(request):
    return render(request, 'speakers/speaker26.html')


def speakerDesc7(request):
    return render(request, 'speakers/speaker27.html')


def speakerDesc8(request):
    return render(request, 'speakers/speaker11.html')


def speakerDesc9(request):
    return render(request, 'speakers/speaker12.html')


def speakerDesc10(request):
    return render(request, 'speakers/speaker13.html')


def speakerDesc11(request):
    return render(request, 'speakers/speaker14.html')


def speakerDesc12(request):
    return render(request, 'speakers/speaker15.html')


def speakerDesc13(request):
    return render(request, 'speakers/speaker16.html')


def speakerDesc14(request):
    return render(request, 'speakers/speaker31.html')


def speakerDesc15(request):
    return render(request, 'speakers/speaker32.html')


def speakerDesc16(request):
    return render(request, 'speakers/speaker33.html')


def speakerDesc17(request):
    return render(request, 'speakers/speaker34.html')


def speakerDesc18(request):
    return render(request, 'speakers/speaker35.html')


def speakerDesc19(request):
    return render(request, 'speakers/speaker36.html')


def speakerDesc20(request):
    return render(request, 'speakers/speaker37.html')


def speakerDesc21(request):
    return render(request, 'speakers/speaker38.html')


def speakerDesc22(request):
    return render(request, 'speakers/speaker39.html')

def memberDesc1(request):
    return render(request, 'about_us/Member1.html')

def memberDesc2(request):
    return render(request, 'about_us/Member2.html')

def memberDesc3(request):
    return render(request, 'about_us/Member3.html')

def memberDesc4(request):
    return render(request, 'about_us/Member4.html')

def memberDesc5(request):
    return render(request, 'about_us/Member5.html')

def memberDesc6(request):
    return render(request, 'about_us/Member6.html')

def memberDesc7(request):
    return render(request, 'about_us/Member7.html')

def memberDesc8(request):
    return render(request, 'about_us/Member8.html')

def memberDesc9(request):
    return render(request, 'about_us/Member9.html')

def memberDesc10(request):
    return render(request, 'about_us/Member10.html')

def memberDesc11(request):
    return render(request, 'about_us/Member11.html')

def memberDesc12(request):
    return render(request, 'about_us/Member12.html')

def memberDesc13(request):
    return render(request, 'about_us/Member13.html')

def memberDesc14(request):
    return render(request, 'about_us/Member14.html')

def memberDesc15(request):
    return render(request, 'about_us/Member15.html')

def memberDesc16(request):
    return render(request, 'about_us/Member16.html')

def memberDesc17(request):
    return render(request, 'about_us/Member17.html')

def memberDesc18(request):
    return render(request, 'about_us/Member18.html')

def memberDesc19(request):
    return render(request, 'about_us/Member19.html')

def memberDesc20(request):
    return render(request, 'about_us/Member20.html')

def memberDesc21(request):
    return render(request, 'about_us/Member21.html')

def memberDesc22(request):
    return render(request, 'about_us/Member22.html')

def memberDesc23(request):
    return render(request, 'about_us/Member23.html')

def memberDesc24(request):
    return render(request, 'about_us/Member24.html')

def memberDesc25(request):
    return render(request, 'about_us/Member25.html')

def memberDesc26(request):
    return render(request, 'about_us/Member26.html')

def memberDesc27(request):
    return render(request, 'about_us/Member27.html')

def memberDesc28(request):
    return render(request, 'about_us/Member28.html')

def memberDesc29(request):
    return render(request, 'about_us/Member29.html')

def memberDesc30(request):
    return render(request, 'about_us/Member30.html')

def memberDesc31(request):
    return render(request, 'about_us/Member31.html')

def memberDesc32(request):
    return render(request, 'about_us/Member32.html')

def memberDesc33(request):
    return render(request, 'about_us/Member33.html')

def memberDesc34(request):
    return render(request, 'about_us/Member34.html')

def memberDesc35(request):
    return render(request, 'about_us/Member35.html')

# linking of studio speakers 2021-22


def speakerDesc100(request):
    return render(request, 'speakers/vr_raman40.html')    


def speakerDesc101(request):
    return render(request, 'speakers/Binayak_41.html')    

def speakerDesc102(request):
    return render(request, 'speakers/Helia42.html')       

def speakerDesc103(request):
    return render(request, 'speakers/Akshita_43.html')          
