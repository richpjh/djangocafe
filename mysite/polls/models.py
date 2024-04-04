from django.db import models

class Question(models.Model):
    drink_type = models.CharField(max_length=200, verbose_name="음료 종류")

    def __str__(self):
        return self.drink_type

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    drink_name = models.CharField(max_length=200, verbose_name="세부 음료 종류")
    votes = models.IntegerField(default=0, verbose_name="투표 수")

    def __str__(self):
        return self.drink_name
