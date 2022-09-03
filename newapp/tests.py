from django.test import TestCase
from .models import Homepage, AboutUs, Subjects, Courses, Students, Teachers, SignUp, Testimonial, OurBlog

class HomepageTestCase(TestCase):
    def create_homepage(self, title="23dededre", text="roar", image="wwwwwwwwwwww" ):
        return Homepage.objects.create(title=title, text=text, image=image)
        
    def test_homepages_creation(self):
        a=self.create_homepage()
        self.assertTrue(isinstance(a, Homepage))
        self.assertEqual(a.title , a.title)
        
class AboutUsTestCase(TestCase):
    def create_aboutus(self, title="23dededre", text="roar", image="wwwwwwwwwwww" ):
        return AboutUs.objects.create(title=title, text=text, image=image)
        
    def test_aboutus_creation(self):
        a=self.create_aboutus()
        self.assertTrue(isinstance(a, AboutUs))
        self.assertEqual(a.title , a.title)

class SubjectsTestCase(TestCase):
    def create_subjects(self, courses_nomber=2, section="roar", image="wwwwwwwwwwww" ):
        return Subjects.objects.create(courses_nomber=courses_nomber, section=section, image=image)
        
    def test_subjects_creation(self):
        a=self.create_subjects()
        self.assertTrue(isinstance(a, Subjects))
        self.assertEqual(a.courses_nomber , a.courses_nomber)
        
class CoursesTestCase(TestCase):
    def create_courses(self, title="23dededre", image="wwwwwwwwwwww", time=5 , person=34, mark=4, price=90 ):
        return Courses.objects.create(title=title, image=image, time=time, person=person, mark=mark, price=price)
        
    def test_courses_creation(self):
        a=self.create_courses()
        self.assertTrue(isinstance(a, Courses))
        self.assertEqual(a.title , a.title)
        
class StudentsTestCase(TestCase):
    def create_students(self, title="23dededre", text="roar",section="sssss", image="wwwwwwwwwwww" ):
        return Students.objects.create(title=title, text=text, image=image, section=section)
        
    def test_students_creation(self):
        a=self.create_students()
        self.assertTrue(isinstance(a, Students))
        self.assertEqual(a.section , a.section)
        
class TeachersTestCase(TestCase):
    def create_teachers(self, name="23dededre",jobs="roar", image="wwwwwwwwwwww" ):
        return Teachers.objects.create(name=name, jobs=jobs, image=image)
        
    def test_teachers_creation(self):
        a=self.create_teachers()
        self.assertTrue(isinstance(a, Teachers))
        self.assertEqual(a.jobs , a.jobs)
        
class SignUpTestCase(TestCase):
    def create_signup(self, name="23dededre", email="roar", course="wwwwwwwwwwww" ):
        return SignUp.objects.create(name=name, email=email, course=course)
        
    def test_signup_creation(self):
        a=self.create_signup()
        self.assertTrue(isinstance(a, SignUp))
        self.assertEqual(a.course , a.course)
        
class TestimonialTestCase(TestCase):
    def create_testimonial(self, name="23dededre", text="roar", image="wwwwwwwwwwww", lavel="kkk" ):
        return Testimonial.objects.create( name=name, text=text, image=image, lavel=lavel)
        
    def test_testimonial_creation(self):
        a=self.create_testimonial()
        self.assertTrue(isinstance(a, Testimonial))
        self.assertEqual(a.name , a.name)
        
       
class OurBlogTestCase(TestCase):
    def create_ourblog(self, text="23dededre", data="roar", image="wwwwwwwwwwww" ):
        return OurBlog.objects.create(text=text, data=data, image=image)
        
    def test_ourblog_creation(self):
        a=self.create_ourblog()
        self.assertTrue(isinstance(a, OurBlog))
        self.assertEqual(a.data , a.data    )
        