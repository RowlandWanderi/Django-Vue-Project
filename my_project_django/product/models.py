from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    # slug is used to get the address of the specific category
    slug = models.SlugField()

    # if we widh to order our categories by name in the database
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    # we need to get the url of the category which we will use in the frontend later
    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
# function to get images    
    def get_image(self):
        # if it exists
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    #function to get thumbnail 
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        #if there is no thumbnail generate one from the image
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
     
     #function to generate thumbnail       
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail