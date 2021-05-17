from django.shortcuts import render
from django.contrib import messages
from blog1.models import contect, post

def home(request):
    allpost = post.objects.all()
    context = {'allpost': allpost}
    return render(request, 'blog/home.html', context)

def basic(request):
    return render(request, 'blog/basic.html')

def news(request, Slug):
    posts = post.objects.filter(title=Slug)

    context = {'posts':posts}


    return render(request, 'blog/blog1.html', context)



def info(request):
    return render(request, 'blog/about.html')

def us(request):
    return render(request, 'blog/contectus.html')





def feedback(request):

    messages.success(request, 'Welcome to feedback.')


    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['text']

        if (name == '') or (email =='') or (phone == '') or len(phone)<10 or (text == ''):
            messages.error(request, 'Please! Fill the form correctly.')
        else:

            contect1 = contect(name=name, email=email, phone=phone, text=text)
            contect1.save()
            messages.success(request, 'Form is Successfully uploaded!')

    return render(request, 'blog/contect2.html')

def search(request):
    #allpost = post.objects.all()
    query = request.GET['query']
    allpost = post.objects.filter(title__icontains=query)
    context = {'allpost': allpost}
    return render(request, 'blog/search.html', context)

