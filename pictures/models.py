from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =50)
     
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self, update):
        self.name = update
        self.save()

    # @classmethod
    # def get_category_id(cls, id):
    #     category = Category.objects.get(pk = id)
    #     return category

    @classmethod
    def search_by_title(cls,search_term):
        category = cls.objects.filter(name__icontains=search_term)
        return category
    
    

class Location(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name

    @classmethod
    def tag_articles(cls):
        tags = cls.objects.all()
        return tags

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.name = update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate = Location.objects.get(pk = id)
        return locate

   

class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    image_name = models.CharField(max_length =30)
    image_description = models.TextField()
    image_location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        )
    image_category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']
