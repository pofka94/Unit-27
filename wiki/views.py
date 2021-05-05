from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse

from .models import Page

# Create your views here.
def index(request):
    page_list = Page.objects.order_by('title')[:5]
    context = {"page_list": page_list,}
    return render(request, "wiki/index.html", context)

    # page_list = Page.objects.order_by('title')[:5]
    # template = loader.get_template("wiki/index.html")
    # context = {"page_list": page_list,}
    # return HttpResponse(template.render(context, request))

    # return HttpResponse("Helo bruda, welcome to mi wrld!?")

def detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, "wiki/detail.html", {"page": page})

    # try:
    #     page = Page.objects.get(pk=page_id)
    # except Page.DoesNotExist:
    #     raise Http404("Page does not exist.")
    # return render(request, "wiki/detail.html", {"page": page})

    # return HttpResponse("You're looking at page %s." % page_id)

def results(request, page_id):
    response = "You're looking at the results of page %s."
    return HttpResponse(response % page_id)