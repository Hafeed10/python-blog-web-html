from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField() 
    description = models.TextField()
    category = models.ManyToManyField(Category)  # Corrected field definition
    time_to_read = models.CharField(max_length=255)
    image = models.ImageField(upload_to="poster/")

    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Corrected field definition
    published_date = models.DateField()  # Changed field name to published_date
    is_draft = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
