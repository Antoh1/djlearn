from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, Http404
from .models import Author, TodoList, Item

# Create your views here.

def Index(request, list_id):
    # try:
    #     tdls = TodoList.objects.get(id=item_id)
    # except TodoList.DoesNotExist:
    #     raise Http404("No such item")
    tdl = get_object_or_404(TodoList, pk=list_id)
    return render(request, 'base/item_list.html',{"tdl": tdl})

def Home(request):
    tl = TodoList.objects.all()
    return render(request, 'base/home.html',{"lnk": tl})


def Status(request, list_id):
    tdl = get_object_or_404(TodoList, pk=list_id)
    try:
        selected_item = tdl.item_set.get(pk=request.POST['item'])
    except (KeyError, Item.DoesNotExist):
        return render(request, 'base/item_list.html',{"tdl": tdl, "error_message": "You did not select a task to complete"})
    else:
        selected_item.completed = True
        selected_item.save()
        return render(request, 'base/item_list.html',{"tdl": tdl})








