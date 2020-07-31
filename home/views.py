from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Index(View):
    def get(self, request):
        # return HttpResponse('test')
        # return render(request, 'home/base.html')
        return render(request, 'home/index.html')