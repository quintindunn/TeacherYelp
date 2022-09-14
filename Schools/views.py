from django.shortcuts import render
from .models import School


def school_index(request, pk_school):
    school_obj = School.objects.get(school_uuid=pk_school)
    ctx = {
        'pk_school': pk_school,
        'school': school_obj,
        'school_rating': school_obj.get_average_teacher_rating(),
        'sorted_teachers': sorted(school_obj.teachers.all(), key=lambda x: x.rating, reverse=True),
        'a-z_sorted_teachers': sorted(school_obj.teachers.all(), key=lambda x: x.last_name)
    }
    print(ctx['sorted_teachers'])
    return render(request, 'schools/school.html', ctx)