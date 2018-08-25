from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


from django.utils.text import slugify
# Create your models here.

def upload_to(instance, filename):
    return '%s%s%s'%('app',instance.slug,filename)

class Post(models.Model):
    user=models.ForeignKey('auth.User' ,verbose_name='Yazar' , on_delete=models.CASCADE ,related_name='posts')
    draft=models.BooleanField(verbose_name='needed to create draft')
    title=models.CharField(max_length=120)
    content=RichTextField()
    image=models.ImageField(blank=True, null=True, upload_to=upload_to)
    publishing_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True, editable=False ,max_length=130)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'slug': self.slug})

    def update_url(self):
        return reverse('app:update', kwargs={'slug': self.slug})

    def create_url(self):
        return reverse('app:create', kwargs={'slug': self.slug})

    def delete_url(self):
        return reverse('app:delete', kwargs={'slug': self.slug})
    def index_url(self):
        return reverse('app:index')

    def url(self):
        self._require_file()
        return self.storage.url(self.name)
    def get_unique_slug(self):
        slug=slugify(self.title)
        unique_slug=slug
        counter = 1
        while Post.objects.filter(slug = unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1

        return unique_slug
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering=['-publishing_date']


class Comment(models.Model):
    post=models.ForeignKey('app.Post', related_name='comments' , on_delete=models.CASCADE )
    name=models.CharField(max_length=200)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name