from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, TodoList, Item

# Create your views here.

def Index(request, item_id):
    #tl = TodoList.objects.get(id=item_id)

    if Item.objects.filter(todolist=item_id):
        items = Item.objects.filter(todolist=item_id)
        itm = Item.objects.get(id=item_id)
    #item_id = 1
    #itm = Item.objects.get(id=item_id)
    print(itm)
    #return HttpResponse("<table><th>Without Reference</th><th>Without Reference2</th><tr><td>%s</td><td>  %s</td><td>  %s</td><td>  %s</td><td>  %s</td></tr></table>" %(tl.title, itm.name, itm.description, itm.completed, itm.date))
    return render(request, 'base/item_list.html',{"tdl": itm.todolist, "iname": itm.name, "items": items})

def Home(request):
    tl = TodoList.objects.all()
    print(type(tl), tl)
    #url = {}
    #for l in tl:
        #url += "<h2><a href='/" + str(l.id) + "'>" + l.title + "</a></h2>" + "\n"
    return render(request, 'base/home.html',{"lnk": tl})
    #return HttpResponse(url)

# def Med(request):
#     return render(request, 'base/index.html')