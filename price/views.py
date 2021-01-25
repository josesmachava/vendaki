from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')



def handler404(request, exception):
      return render(request, 'error/404.pug', status=404)


def handler500(request, *args, **argv):
    return render(request, 'error/500.jade', status=500)