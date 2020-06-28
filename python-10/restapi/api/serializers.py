from rest_framework import serializers


class QuestionSerializer(serializers.Serializer):
    question = serializers.ListField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass