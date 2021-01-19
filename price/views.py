import random
import string

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.template import RequestContext
from django.core.files.base import ContentFile

from django.utils.decorators import method_decorator
from django.views.generic import View, DeleteView, DetailView, ListView
import qrcode



# Create your views here.


def index(request):
    return render(request, 'index.html')



def handler404(request, exception):
    return render(request, 'error/404.jade', status=404)

def handler500(request):
    return render(request, 'error/500.jade', status=500)