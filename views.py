import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
    ''')

def about(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    # content_html = open ("content/index.html").read()
    # response = requests.get('https://api.github.com/users/samfrida/repos')
    # repos = response.json()
    context = {}
    # return render(request, "base.html", context)
    return render(request, "content/index.html", context)


def experience(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    # content_html = open ("content/Experience.html").read()
    context = {
        # 'content': content_html,
        # 'title':"Experience"
    }
    return render(request, "content/Experience.html", context)

def education(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    # content_html = open ("content/Education.html").read()
    context = {
        # 'content': content_html,
        # 'title':"Education"
    }
    return render(request, "content/Education.html", context)

def interest(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    # content_html = open ("content/Interest.html").read()
    context = {
        # 'content': content_html,
        # 'title':"Interest"
    }
    return render(request, "content/Interest.html", context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/samfrida/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

