from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util
from random import randint


class wikiContentForm(forms.Form):
    title = forms.CharField(max_length=30)
    content = forms.CharField(widget = forms.Textarea( attrs={'rows':10,'columns':20}) )

content = []

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def NewPage(request):
    WikiPage = wikiContentForm()
    if request.method == "POST":
        WikiPage = wikiContentForm(request.POST)
        if WikiPage.is_valid():
            util.save_entry(WikiPage.cleaned_data['title'], WikiPage.cleaned_data['content'])
            return HttpResponseRedirect(reverse("index")) 
        else:
            return render(request, "encyclopedia/NewPage.html", {
                'WikiPage': WikiPage
            },)
            
    return render(request, "encyclopedia/NewPage.html",{
        "WikiPage": WikiPage
    })
    
def RandomPage(request):
    atuaispaginas = util.list_entries()
    title = atuaispaginas[randint(0,len(atuaispaginas)-1 )]
    pagina = util.Convert_to_html(title)
    return render(request, "encyclopedia/AnyWikiFile.html", {
        'title':title,
        'pagina':pagina
        })

def MD_render(request, name):
 
    pagina = util.Convert_to_html(name)
    wikipage = HttpResponse(pagina)
    return render(request, "encyclopedia/AnyWikiFile.html",
     {
        'title':name,
        'pagina':pagina
        }
     )