from django.shortcuts import get_object_or_404

from rest_framework import viewsets, generics, views, status
from rest_framework.response import Response

from course.paginators import CourseAndLessonPagination
from users.permissions import IsModerator, IsOwner
from rest_framework.permissions import IsAuthenticated

from course.models import Course, Lesson, Subscription
from course.serliazers import CourseSerializers, LessonSerializers, CourseDetailSerializers
from users.tasks import sub_update


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    filterset_fields = ('course_name',)
    queryset = Course.objects.all()
    pagination_class = CourseAndLessonPagination

    def update(self, request, pk=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = self.get_serializer(course, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            sub_update.delay(pk)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        elif self.action == 'update':
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializers
        return CourseSerializers

    def perform_create(self, serializer):
        course = serializer.save(owner=self.request.user)
        course.save()

    def get(self, request):
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = CourseSerializers(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class SubscriptionAPIView(views.APIView):

    def post(self, *args, **kwargs):
        course_id = self.kwargs.get("pk")
        course = get_object_or_404(Course, pk=course_id)
        is_subscribe = self.request.data.get("subscribe")
        user = self.request.user

        if is_subscribe:
            subscription = user.subscriptions.create(user=user, course=course)
            subscription.save()
            message = f"You've successfully subscribed for '{course.name}'"
        else:
            Subscription.objects.filter(user=user, course=course).delete()
            message = f"Your subscription for '{course.name}' has been cancelled."
        return Response({"message": message})


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        lesson = serializer.save(owner=self.request.user)
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]
    pagination_class = CourseAndLessonPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated,IsModerator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated,IsOwner]

