from django.db import models

# Create your models here.
# I need to look how we can get an array in models view without dependance of database. 
# For example field should have (text + its background color). 
# Real example,   introduction = ['blue', 'Thesis introduction']
# Actually this could be done using postgres listField or mysql, client wanted us
# not to be specific to db. I will reach out to check out on the same as we develop. 

class DefaultTemplate(models.Model):
    # Default Tmeplate model and its fields
    # This is just an example but modifications will be done
    slug = models.SlugField(unique=True, primary_key=True, blank=True, max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    documenttype = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    introduction = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    literaturereview = models.TextField(blank=True)
    conclusion = models.TextField(blank=True)
    references = models.TextField(blank=True)

    def __str__(self):
        return self.title
