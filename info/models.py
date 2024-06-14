from django.db import models

class Subject(models.Model):

    subject = models.CharField(max_length=100)
    accord = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.subject




class Question(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='')
    question = models.CharField(max_length=600)
    answer = models.TextField()

    def __str__(self):
        return self.question

