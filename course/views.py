from rest_framework import viewsets, generics

from course.models import Course, Lesson
from course.serliazers import CourseSerializers, LessonSerializers, CourseDetailSerializers
# from course.serliazers import CourseSerializers, LessonSerializers, CourseDetailSerializers

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    filterset_fields = ('course_name',)
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializers
        return CourseSerializers


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()

