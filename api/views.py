from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import JackRateThrottle
from .models import Student
from .serializers import StudentSerializer


# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     authentication_classes = [SessionAuthentication]
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    throttle_classes = [AnonRateThrottle, JackRateThrottle]
