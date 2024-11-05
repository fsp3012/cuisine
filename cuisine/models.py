from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('published', 'Published')
)

CATG_CHOICE = (
    ('dessert', 'Dessert'),
    ('snack', 'Snack'),
    ('food', 'Food')
)


class Cuisine(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=8,
                                choices=(('veg', 'Veg'), ('non veg', 'NV')),
                                default='non veg')
    catg = models.CharField(max_length=8, 
                                choices=CATG_CHOICE,
                                default='food')
    slug = models.SlugField(max_length=30, unique_for_date='publish')
    desc = models.TextField()
    pic = models.ImageField(upload_to='cuisine_pic', blank=True, null=True)
    author = models.ForeignKey(User, 
                                related_name='cuisine_user',
                                on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                    choices=STATUS_CHOICE,
                                    default='draft')
    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cuisine:Cuisine_detail", 
                        args=[self.slug]
                        )
