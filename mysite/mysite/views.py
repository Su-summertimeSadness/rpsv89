from django.shortcuts import render, redirect
from django.views import View
from .models import Name

# Create your views here.
class Index(View):
    model = Name.objects.all()

    def get(self, request):
        return render(request, 'mysite/index.html')

class MakeData(View):

    def get(self, request):
        return render(request, 'mysite/index.html')

    def post(self, request, *args, **kwargs):
        data = request.POST
        record = Name.objects.create(data=data)
        record.save()
        return redirect('show')

class Show(View):
    def get(self, request):
        data = Name.objects.all()
        data = list(data)
        return render(request, 'mysite/show.html', context={'data': data})
