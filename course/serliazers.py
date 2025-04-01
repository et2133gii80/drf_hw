from rest_framework import serializers


from course.models import Course, Lesson
from course.validators import UrlValidator
from course.models import Subscription


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url')]


class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializers(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializers(many=True)
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, course):
        user = self.context.get("request").user
        return Subscription.objects.filter(user=user, course=course).exists()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("course_name", "preview", "description", "number_of_lessons", "lessons", "is_subscribed")