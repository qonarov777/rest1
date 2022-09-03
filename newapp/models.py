from django.db import models
from distutils.command.upload import upload

class Homepage(models.Model):
    title=models.CharField( max_length=50)
    text= models.TextField(max_length=500)
    image=models.ImageField(upload_to='media/home/')

    class Meta:
        verbose_name ='Reklama'
        verbose_name_plural='Reklamalar'
      

    def __str__(self):
        return self.title
    
class AboutUs(models.Model):
    title=models.CharField( max_length=50)
    text= models.TextField(max_length=500)
    image=models.ImageField(upload_to='media/about/')
    

    class Meta:
        verbose_name ='Biz haqimizda'
        verbose_name_plural='Biz haqimizda'

    def __str__(self):
        return self.title

   
class Subjects(models.Model):
    courses_nomber=models.IntegerField()
    section= models.TextField(max_length=500)
    image=models.ImageField(upload_to='media/subjects/')
    

    class Meta:
        verbose_name = 'Mavzu'
        verbose_name_plural='Mavzular'

    def __str__(self):
        return self.section


class Courses(models.Model):
    time=models.IntegerField()
    person= models.IntegerField()
    title= models.TextField(max_length=100)
    image=models.ImageField(upload_to='media/Courses/')
    mark=models.IntegerField()
    price=models.IntegerField()

    class Meta:
        verbose_name = 'Kurs'
        verbose_name_plural='Kurslar'

    def __str__(self):
        return self.title
    
    
class Students(models.Model):
    
    title= models.TextField(max_length=50)
    text= models.TextField(max_length=200)
    section= models.TextField(max_length=50)
    image=models.ImageField(upload_to='media/subjects/')
    

    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural='Yangiliklar'

    def __str__(self):
        return self.section
    
    
class SignUp(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.EmailField( max_length=54)
    course=models.CharField( max_length=50)

    class Meta:
        verbose_name = 'Royxatdan o`tish`'
        verbose_name_plural='Ro`yxatgan o`tganlar'

    def __str__(self):
        return self.name
    
    
class Teachers(models.Model):
    
    name=models.CharField(max_length=50)
    jobs=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/Teachers/')

    class Meta:
        verbose_name = 'O`qituvchi'
        verbose_name_plural='O`qituvchilar'

    def __str__(self):
        return self.name
    
    
class Testimonial(models.Model):
    
    text= models.TextField(max_length=200)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/Teachers/')
    lavel=models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural='Professorlar'

    def __str__(self):
        return self.name
    
class OurBlog(models.Model):
    
    text= models.TextField(max_length=200)
    data=models.CharField(max_length=50)
    image=models.ImageField(upload_to='media/Teachers/')
    

    class Meta:
        verbose_name = 'Guruh'
        verbose_name_plural='Guruhlar'

    def __str__(self):
        return self.data