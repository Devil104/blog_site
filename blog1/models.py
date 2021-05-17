from django.db import models




class contect(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=13)
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message from '+ self.name+'-'+ self.email


class post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(max_length=100000000)
    slug = models.SlugField(max_length=50)
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image/')
    timestamp = models.DateTimeField( blank=True)

    def __str__(self):
        return 'Blog title:'+ self.title +' by '+ self.author



