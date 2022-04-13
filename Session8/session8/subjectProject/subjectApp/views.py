from django.shortcuts import render #redirect
from .models import Major, Subject
from django.views.generic import CreateView #UpdateView
from .forms import MajorModelForm, SubjectModelForm
from django.urls import reverse_lazy

# Create your views here.
class AddMajorView(CreateView):
    model = Major
    form_class = MajorModelForm
    template_name = 'addMajor.html'
    success_url = reverse_lazy('home')

class AddSubjectView(CreateView):
    model = Subject
    form_class = SubjectModelForm
    template_name = 'addSubject.html'
    success_url = reverse_lazy('home')


class computerSubjectView(request):
    subject = Subject.objects.all()
    computerMajor= subject.filter(major__name='컴퓨터학과')

    return render(request, 'computer.html', {'computerMajor': computerMajor})

def home(request):
    majors = Major.objects.all()
    subjects = Subject.objects.all()

    return render(request, 'home.html', { 'subjects' : subjects, 'majors' : majors })