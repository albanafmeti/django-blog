from django.shortcuts import render
from blog.models import Post
from django.http import JsonResponse
from django.core.mail import send_mail


def index(request):
    posts = Post.objects.all().order_by('-id')[:4]
    return render(request, "blog/index.html", context={"posts": posts})


def get_all(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, "blog/all.html", context={"posts": posts})


def show(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, "blog/show.html", context={"post": post})


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


def contact_send(request):
    name = request.POST['name'][0]
    email = request.POST['email'][0]
    phone = request.POST['phone'][0]
    message = request.POST['message'][0]

    send_mail(
        'New contact message',
        message,
        name + " <" + email + ">",
        ['albanafmeti@gmail.com'],
        fail_silently=True,
    )

    return JsonResponse({
        "success": True
    })
