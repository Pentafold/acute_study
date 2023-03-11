from rest_framework import serializers
from .models import Course, Module, Chapter


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['name', 'position']


class ModuleSerializer(serializers.ModelSerializer):
    submodule = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ['name', 'position', 'submodule', 'chapter']

    def get_submodule(self, obj):
        return ModuleSerializer(obj.submodules, many=True).data

    def get_chapter(self, obj):
        return ChapterSerializer(obj.chapters, many=True).data


class CourseSerializer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['name', 'modules']

    def get_modules(self, obj):
        return ModuleSerializer(obj.modules, many=True).data
