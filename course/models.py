from django.db import models

from common.models import BaseModel


class Course(BaseModel):
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=500, null=False)
    instructor = models.CharField(max_length=50, null=True)
    price = models.FloatField()

    @property
    def modules(self):
        return Module.objects.filter(is_submodule=False).order_by('position').all()


class Module(BaseModel):
    name = models.CharField(max_length=50, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    position = models.IntegerField()
    is_submodule = models.BooleanField(default=False)

    @property
    def submodules(self):
        return [submodule.child for submodule in SubModule.objects.filter(parent=self).order_by('position').all()]

    @property
    def chapters(self):
        return Chapter.objects.filter(module=self).order_by('position').all()


class SubModule(BaseModel):
    parent = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='parent')
    child = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='child')
    position = models.IntegerField()


class Chapter(BaseModel):
    name = models.CharField(max_length=50, null=False)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    position = models.IntegerField()
