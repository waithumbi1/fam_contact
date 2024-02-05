from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymember = Member.objects.all().order_by("firstName", "-id").values()
    template = loader.get_template('display.html')

    context = {
        'mymembers': mymember
    }

    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')

    context = {
        'mymember': mymember
    }

    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['mango', 'apple', 'banana']
    }
    return HttpResponse(template.render(context, request))
