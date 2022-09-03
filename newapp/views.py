from django.shortcuts import render
from rest_framework.generics import DestroyAPIView,RetrieveAPIView, UpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import  IsAdminUser
from .models import AboutUs
from .serializers import AboutUsSerializer, HomepageSerializer, SubjectsSerializer, CoursesSerializer, StudentsSerializer, SignUpSerializer, TeachersSerializer, TestimonialSerializer, OurBlogSerializer

from .models import Homepage, Subjects, Courses, Students, SignUp, Teachers, Testimonial, OurBlog

  
    # Homepage uchun viewlar -----------------------------------------------------

# post yangi objecty qoshadi
class CreateHomepage(CreateAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    permission_classes = [IsAdminUser]

# get malumotni chiqarib berish
class ListHomepage(ListAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    permission_classes = [IsAdminUser]

# delate malumotlarni ochirish id orqali
class DestroyHomepage(DestroyAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    permission_classes = [IsAdminUser]

# get= malumotni chiqarib berish
class RetrieveHomepage(RetrieveAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    permission_classes = [IsAdminUser]

# put, patch malumotni tahrirlash
class UpdateHomepage(UpdateAPIView):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    permission_classes = [IsAdminUser]    
    

# AboutUs uchun viewlar----------------------------------------------------------
# post yangi objecty qoshadi 
class CreateAboutUs(CreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]

# get malumotni chiqarib berish
class ListAboutUs(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]
    
# delate malumotlarni ochirish id orqali
class DestroyAboutUs(DestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]

# get= malumotni chiqarib berish
class RetrieveAboutUs(RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]

# put, patch malumotni tahrirlash
class UpdateAboutUs(UpdateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [IsAdminUser]
  
    
#   Subjects modeliga =============================================

class CreateSubjects(CreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    permission_classes = [IsAdminUser]

# get malumotni chiqarib berish
class ListSubjects(ListAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    permission_classes = [IsAdminUser]

# delate malumotlarni ochirish id orqali
class DestroySubjects(DestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    permission_classes = [IsAdminUser]

# get= malumotni chiqarib berish
class RetrieveSubjects(RetrieveAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    permission_classes = [IsAdminUser]

# put, patch malumotni tahrirlash
class UpdateSubjects(UpdateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    permission_classes = [IsAdminUser]    
    
    
#   Courses modeliga =============================================

class CreateCourses(CreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAdminUser]

# get malumotni chiqarib berish
class ListCourses(ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAdminUser]

# delate malumotlarni ochirish id orqali
class DestroyCourses(DestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAdminUser]

# get= malumotni chiqarib berish
class RetrieveCourses(RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAdminUser]

# put, patch malumotni tahrirlash
class UpdateCourses(UpdateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAdminUser]    
    
    
   
#   Students modeliga =============================================

class CreateStudents(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAdminUser]

# get malumotni chiqarib berish
class ListStudents(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAdminUser]

# delate malumotlarni ochirish id orqali
class DestroyStudents(DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAdminUser]

# get= malumotni chiqarib berish
class RetrieveStudents(RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAdminUser]

# put, patch malumotni tahrirlash
class UpdateStudents(UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAdminUser]    
    
  
#   SignUp modeliga =============================================

class CreateSignUp(CreateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [IsAdminUser]

# get malumotni chiqarib berish
class ListSignUp(ListAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [IsAdminUser]

# delate malumotlarni ochirish id orqali
class DestroySignUp(DestroyAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [IsAdminUser]

# get= malumotni chiqarib berish
class RetrieveSignUp(RetrieveAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [IsAdminUser]

# put, patch malumotni tahrirlash
class UpdateSignUp(UpdateAPIView):
    queryset = SignUp.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [IsAdminUser]    
    
    
  
#   Teachers modeliga =============================================

class CreateTeachers(CreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAdminUser]

# get malumotni chiqarib berish
class ListTeachers(ListAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAdminUser]

# delate malumotlarni ochirish id orqali
class DestroyTeachers(DestroyAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAdminUser]

# get= malumotni chiqarib berish
class RetrieveTeachers(RetrieveAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAdminUser]

# put, patch malumotni tahrirlash
class UpdateTeachers(UpdateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    permission_classes = [IsAdminUser]    
    

#   Testimonial modeliga =============================================

class CreateTestimonial(CreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAdminUser]

# get malumotni chiqarib berish
class ListTestimonial(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAdminUser]

# delate malumotlarni ochirish id orqali
class DestroyTestimonial(DestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAdminUser]

# get= malumotni chiqarib berish
class RetrieveTestimonial(RetrieveAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAdminUser]

# put, patch malumotni tahrirlash
class UpdateTestimonial(UpdateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = [IsAdminUser]    
    

#   OurBlog modeliga =============================================

class CreateOurBlog(CreateAPIView):
    queryset = OurBlog.objects.all()
    serializer_class = OurBlogSerializer
    permission_classes = [IsAdminUser]

# get malumotni chiqarib berish
class ListOurBlog(ListAPIView):
    queryset = OurBlog.objects.all()
    serializer_class = OurBlogSerializer
    permission_classes = [IsAdminUser]

# delate malumotlarni ochirish id orqali
class DestroyOurBlog(DestroyAPIView):
    queryset = OurBlog.objects.all()
    serializer_class = OurBlogSerializer
    permission_classes = [IsAdminUser]

# get= malumotni chiqarib berish
class RetrieveOurBlog(RetrieveAPIView):
    queryset = OurBlog.objects.all()
    serializer_class = OurBlogSerializer
    permission_classes = [IsAdminUser]

# put, patch malumotni tahrirlash
class UpdateOurBlog(UpdateAPIView):
    queryset = OurBlog.objects.all()
    serializer_class = OurBlogSerializer
    permission_classes = [IsAdminUser]    