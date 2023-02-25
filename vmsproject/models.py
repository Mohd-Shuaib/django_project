from django.db import models

# Create your models here.
class TopContent(models.Model):
    
    top_name = models.CharField(max_length=200)
    top_dec = models.TextField()
    top_image = models.ImageField(upload_to='vmsproject/images', default="")
    top_btn = models.CharField(max_length=50)
    def __str__(self):
        return self.top_name

        
class AboutText(models.Model):
    
    about_subtitle1 = models.CharField(max_length=200, default="")
    about_subtitle2 = models.CharField(max_length=200, default="")
    about_subtitle3 = models.CharField(max_length=200, default="")
    about_years = models.CharField(max_length=50,default="")
    about_para1 = models.TextField(default="")
    about_para2 = models.TextField(default="")
    about_para3 = models.TextField(default="")
    about_para4 = models.TextField(default="")
    about_img1 = models.ImageField(upload_to='vmsproject/images', default="")
    about_img2 = models.ImageField(upload_to='vmsproject/images', default="")
    about_img3 = models.ImageField(upload_to='vmsproject/images', default="")
    about_img4 = models.ImageField(upload_to='vmsproject/images', default="")

    def __str__(self):
        return self.about_subtitle1


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_dec = models.TextField(default="")
    product_date = models.DateField()
    product_image = models.ImageField(upload_to='vmsproject/images', default="")

    def __str__(self):
        return self.product_name


class Product_Title(models.Model):
    sub_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.sub_title
  

class Exhibition(models.Model):
    exhibition_image = models.ImageField(upload_to='vmsproject/images', default="")

    def __str__(self):
        return str(self.exhibition_image)


class Exhibition_Title(models.Model):
    sub_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.sub_title

class Team(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=300)
    image = models.ImageField(upload_to='vmsproject/images', default="")
    social_icons = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Team_Title(models.Model):
    sub_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.sub_title


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    dec = models.TextField(default="")
    designation = models.CharField(max_length=300)
    image = models.ImageField(upload_to='vmsproject/images', default="")

    def __str__(self):
        return self.name

class Testimonial_Title(models.Model):
    sub_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.sub_title

class Partner(models.Model):
    image = models.ImageField(upload_to='vmsproject/images', default="")

    def __str__(self):
        return str(self.image)

class Partner_Title(models.Model):
    sub_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.sub_title
   

class Services(models.Model):
    title = models.CharField(max_length=600)
    dec = models.TextField(default="")
    image1 = models.ImageField(upload_to='vmsproject/images', default="")
    image2 = models.ImageField(upload_to='vmsproject/images', default="")

    def __str__(self):
        return str(self.title)


class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     subject= models.CharField(max_length=500)
     message= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email


class Contact_info(models.Model):
    
     title= models.CharField(max_length=255)
     dec= models.TextField()
     address= models.CharField(max_length=100)
     email= models.CharField(max_length=100)
     num1= models.CharField(max_length=500)
     num2= models.CharField(max_length=500)

     def __str__(self):
          return self.title



class Topbar(models.Model):
    
    
     info= models.CharField(max_length=100)
     email= models.CharField(max_length=100)
     num1= models.CharField(max_length=500)
     social_icons = models.BooleanField(default=False)

     def __str__(self):
          return self.info



class Navigationbar(models.Model):
    
     url = models.URLField(max_length=200)
     title= models.CharField(max_length=255)
     pos= models.CharField(max_length=255)


     

     def __str__(self):
          return self.title
     def is_active(self):
          return self.title


class thanks(models.Model):
     title= models.CharField(max_length=255)
     dec= models.TextField()
     Button_Text= models.CharField(max_length=255)

     def __str__(self):
          return self.title