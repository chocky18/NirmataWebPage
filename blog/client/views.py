from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', {})


def post(request):
    return render(request, 'blog/post.html', {})

def post2(request):
    return render(request, 'blog/post2.html', {})

def post3(request):
    return render(request, 'blog/post3.html', {})


def about(request):
    return render(request, 'blog/about.html', {})


def contact(request):
    return render(request, 'blog/contact.html', {})
