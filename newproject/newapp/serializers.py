from rest_framework import serializers
from .models import AboutUs
from .models import Homepage

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
        
        
class HomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homepage
        fields = '__all__'