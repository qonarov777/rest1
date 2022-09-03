from django.contrib import admin
from .models import Homepage
from .models import AboutUs, Subjects, Courses, Students, SignUp, Teachers, Testimonial, OurBlog

admin.site.register(Homepage)
admin.site.register(AboutUs)

admin.site.register(Subjects)
admin.site.register(Courses)
admin.site.register(Students)
admin.site.register(SignUp)
admin.site.register(Teachers)
admin.site.register(Testimonial)
admin.site.register(OurBlog)

