from django.db import models
from tinymce.models import HTMLField
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    

    class Meta:
        verbose_name_plural = ('categories')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,
                            help_text="Slug will be generated automatically from the title of the post")
    body = HTMLField()
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/', blank=True, null=True)
    date_added = models.DateField()
    category = models.ForeignKey('Category', to_field='name', on_delete=models.PROTECT)
    class Meta:
        ordering = ['-date_added',]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
