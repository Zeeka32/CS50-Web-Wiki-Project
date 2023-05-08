from django.shortcuts import render
import markdown2, random
from . import util

def loadEntry(request, name):
    pageEntry = util.get_entry(name)
    if pageEntry == None: 
        return render(request, "encyclopedia/errors/notFound.html")

    html = markdown2.markdown(pageEntry)
    return render(request, "encyclopedia/entry.html", {
        "title" : name,
        "page" : html,
    })


def search(request):

    query = request.GET.get("q")
    pageEntry = util.get_entry(query)

    if pageEntry == None:
        result = []
        entries = util.list_entries()

        for entry in entries:
            if query.lower() in entry.lower():
                result.append(entry)

        return render(request, "encyclopedia/results.html", {
            "entries": result
        })

    html = markdown2.markdown(pageEntry)
    return render(request, "encyclopedia/entry.html", {
        "title": query,
        "page": html,
    })


def createEntry(request):

    if request.method != "POST":
        return render(request, "encyclopedia/createPage.html", {
            "error":"",
            "title": "",
            "content": ""
        })

    title = request.POST.get("title")
    content = request.POST.get("content")

    if title == "" or content == "":
        return render(request, "encyclopedia/createPage.html", {
            "error": "emptyField",
            "title": title,
            "content": content
        })

    if util.get_entry(title) != None:
        return render(request, "encyclopedia/createPage.html", {
            "error": "entryExists",
            "title": title,
            "content": content
        })
    
    util.save_entry(title, content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "page": markdown2.markdown(content)
    })


def editPage(request):

    if request.method != "POST":
        return render(request, "encyclopedia/errors/notFound.html")
    
    title = request.POST.get("title")
    content = request.POST.get("content")

    if content == "":
        return render(request, "encyclopedia/editPage.html", {
            "error": "emptyField",
            "title": title,
            "content": content
        })
    
    util.save_entry(title, content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "page": markdown2.markdown(content)
    })


def editPageRender(request):

    if request.method != "POST":
        return render(request, "encyclopedia/errors/notFound.html")

    title = request.POST.get("title")
    content = util.get_entry(title)
    return render(request, "encyclopedia/editPage.html", {
        "error":"",
        "title": title,
        "content": content,
    })


def randomEntry(request):
    entries = util.list_entries()
    luckyEntry = random.choice(entries)
    entry = util.get_entry(luckyEntry)

    html = markdown2.markdown(entry)
    return render(request, "encyclopedia/entry.html", {
        "title" : luckyEntry,
        "page" : html,
    })


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
