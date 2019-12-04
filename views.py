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
    response = requests.get('https://api.github.com/users/samfrida/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, "index.html", context)


def experience(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'github_repos': repos,
    }
    return render(request, "Experience.html", context)

def education(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'github_repos': repos,
    }
    return render(request, "Education.html", context)

def interest(request):
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'github_repos': repos,
    }
    return render(request, "Interest.html", context)


def github_api_example(request):
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/samfrida/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'github.html', context)

