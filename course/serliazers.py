from rest_framework import serializers

from course.models import Course, Lesson


class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        models = Course
        fields = '__all__'


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        models = Lesson
        fields = '__all__'