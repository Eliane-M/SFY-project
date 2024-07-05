from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from agri.models import SkillAssessment
from agri.serializers import SkillAssessmentSerializer


@api_view(['GET'])
@permission_classes([])
def skill_assessment_list(request):
    if request.method == 'GET':
        skill_assessments = SkillAssessment.objects.all()
        serializer = SkillAssessmentSerializer(skill_assessments, many=True)
        return Response(serializer.data)