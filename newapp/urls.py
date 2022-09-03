from .views import DestroyAboutUs,RetrieveAboutUs, UpdateAboutUs, CreateAboutUs, ListAboutUs
from .views import RetrieveHomepage,DestroyHomepage, UpdateHomepage, ListHomepage, CreateHomepage
from .views import CreateSubjects, ListSubjects, UpdateSubjects, DestroySubjects, RetrieveSubjects
from .views import CreateCourses, ListCourses, UpdateCourses, DestroyCourses, RetrieveCourses
from .views import CreateStudents, ListStudents, UpdateStudents, DestroyStudents, RetrieveStudents
from .views import CreateSignUp, ListSignUp, UpdateSignUp, DestroySignUp, RetrieveSignUp
from .views import CreateTeachers, ListTeachers, UpdateTeachers, DestroyTeachers, RetrieveTeachers
from .views import CreateTestimonial, ListTestimonial, UpdateTestimonial, DestroyTestimonial, RetrieveTestimonial
from .views import CreateOurBlog, ListOurBlog, UpdateOurBlog, DestroyOurBlog, RetrieveOurBlog
from django.urls import path
# from api import views


urlpatterns = [
    
    path('homepage-create/',CreateHomepage.as_view()),
    path('homepage-list/',ListHomepage.as_view()),
    path('homepage-update/<int:pk>',UpdateHomepage.as_view()),
    path('homepage-delete/<int:pk>', DestroyHomepage.as_view()),
    path('homepage-retrieve/<int:pk>', RetrieveHomepage.as_view()),
    
    path('aboutus-create/',CreateAboutUs.as_view()),
    path('aboutus-list/',ListAboutUs.as_view()),
    path('aboutus-update/<int:pk>',UpdateAboutUs.as_view()),
    path('aboutus-delete/<int:pk>', DestroyAboutUs.as_view()),
    path('aboutus-retrieve/<int:pk>', RetrieveAboutUs.as_view()),
    
    path('subjects-create/',CreateSubjects.as_view()),
    path('subjects-list/',ListSubjects.as_view()),
    path('subjects-update/<int:pk>',UpdateSubjects.as_view()),
    path('subjects-delete/<int:pk>', DestroySubjects.as_view()),
    path('subjects-retrieve/<int:pk>', RetrieveSubjects.as_view()),
    
    path('courses-create/',CreateCourses.as_view()),
    path('courses-list/',ListCourses.as_view()),
    path('courses-update/<int:pk>',UpdateCourses.as_view()),
    path('courses-delete/<int:pk>', DestroyCourses.as_view()),
    path('courses-retrieve/<int:pk>', RetrieveCourses.as_view()),
    
    path('students-create/',CreateStudents.as_view()),
    path('students-list/',ListStudents.as_view()),
    path('students-update/<int:pk>',UpdateStudents.as_view()),
    path('students-delete/<int:pk>', DestroyStudents.as_view()),
    path('students-retrieve/<int:pk>', RetrieveStudents.as_view()),
    
    path('signup-create/',CreateSignUp.as_view()),
    path('signup-list/',ListSignUp.as_view()),
    path('signup-update/<int:pk>',UpdateSignUp.as_view()),
    path('signup-delete/<int:pk>', DestroySignUp.as_view()),
    path('signup-retrieve/<int:pk>', RetrieveSignUp.as_view()),
    
    path('teachers-create/',CreateTeachers.as_view()),
    path('teachers-list/',ListTeachers.as_view()),
    path('teachers-update/<int:pk>',UpdateTeachers.as_view()),
    path('teachers-delete/<int:pk>', DestroyTeachers.as_view()),
    path('teachers-retrieve/<int:pk>', RetrieveTeachers.as_view()),
    
    path('testimonial-create/',CreateTestimonial.as_view()),
    path('testimonial-list/',ListTestimonial.as_view()),
    path('testimonial-update/<int:pk>',UpdateTestimonial.as_view()),
    path('testimonial-delete/<int:pk>', DestroyTestimonial.as_view()),
    path('testimonial-retrieve/<int:pk>', RetrieveTestimonial.as_view()),
    
    path('ourblog-create/',CreateOurBlog.as_view()),
    path('ourblog-list/',ListOurBlog.as_view()),
    path('ourblog-update/<int:pk>',UpdateOurBlog.as_view()),
    path('ourblog-delete/<int:pk>', DestroyOurBlog.as_view()),
    path('ourblog-retrieve/<int:pk>', RetrieveOurBlog.as_view()),
    
    
]