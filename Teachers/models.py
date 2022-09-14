from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100)
    image = models.URLField(max_length=100, blank=True, null=True)
    rating = models.FloatField()
    ratings = models.ManyToManyField("Rating", blank=True, related_name="teachers")

    def get_average_rating(self):
        avg = 0
        ratings = self.ratings.all()
        rating_count = len(ratings)
        for rating in ratings:
            avg += rating.rating

        if rating_count > 0:
            return avg / rating_count
        else:
            return 0

    def save(self, *args, **kwargs):
        self.rating = self.get_average_rating()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Rating(models.Model):
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, related_name="teacher")
    rating = models.FloatField()
    comment = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher} | {self.rating} | {self.comment} | {self.date}"