from django.shortcuts import render
from .models import Course
from .serializer import CourseSerializer
from common.views import BaseApiView


class TestAPI(BaseApiView):
    def get(self, request):
        return self.render_response(
            CourseSerializer(Course.objects.all(), many=True).data,
            True,
            None,
            data_to_list=False
        )

