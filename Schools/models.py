from django.db import models


class School(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=100)
    description = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    teachers = models.ManyToManyField("Teachers.Teacher", blank=True, related_name="schools")
    school_uuid = models.CharField(max_length=100, blank=True, null=True)

    def get_average_teacher_rating(self):
        avg = 0
        teachers = self.teachers.all()
        teacher_count = len(teachers)
        for teacher in teachers:
            avg += teacher.rating

        if teacher_count > 0:
            return avg / teacher_count
        else:
            return 0

    def __str__(self):
        return f"{self.name} | {self.address}  {self.city}  {self.state}  {self.zip_code} | {self.school_uuid}"
