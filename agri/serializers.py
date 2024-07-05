from rest_framework import serializers
from django.contrib.auth.models import User
from agri.models import Account, EducationalResources, Employer, SkillAssessment, Joblisting


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
        
class AccountSerializer(serializers.Serializer):
    class Meta:
        model = Account
        fields = "__all__"

class SkillAssessmentSerializer(serializers.Serializer):
    class Meta:
        model = SkillAssessment
        fields = "__all__"

class EducationalResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalResources
        fields = "__all__"

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"

class JoblistingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joblisting
        fields = "__all__"