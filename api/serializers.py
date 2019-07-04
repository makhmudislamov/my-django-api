from rest_framework import serializers
from .models import Assignment, Question, Choice
from users.models import User


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

class QuestionSerializer(serializers.ModelSerializer):
    choices = StringSerializer(many=True)
    class Meta:
        model = Question
        fields = ('id', 'choices', 'question', 'order')

class AssignmentSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    teacher = StringSerializer(many=False)
    class Meta:
        model = Assignment
        fields = ('__all__')

    def get_questions(self, obj):
        questions = QuestionSerializer(obj.questions.all(), many=True).data
        return questions

    def create(self, request):
        data = request.data

        # saving assignment
        assignment = Assignment()
        teacher = User.objects.get(username=data['teacher'])
        assignment.teacher = teacher
        assignment.title = data['title']
        assignment.save()

        # creating question
        order = 1
        for q in data['questions']:
            newQ = Question()
            newQ.question = q['title']
            newQ.order = order
            newQ.save()
        # choices
            for c in q['choices']:
                newC = Choice()
                newC.title = c
                newC.save()
                newQ.choices.add(newC)
        # correct answer
            newQ.answer = Choice.objects.get(title=q['answer'])
            newQ.assignment = assignment
            newQ.save()
            order += 1
        return assignment