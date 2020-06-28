from collections import Counter
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response

# Create your views here.

class QuestionSerializer(serializers.Serializer):
    question = serializers.ListField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

@api_view(["POST"])
def lambda_function(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        question = serializer.data.get('question')
        ordered = orderedNumbers(question)
        return Response(ordered)

def orderedNumbers(numbers):
    solution =[item for items, count in Counter(numbers).most_common() for item in [items] * count]
    response = {"solution": solution}
    return response