from django.db import models

class Subject(models.Model):

    subject = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.subject

    def get_friendly_name(self):
        return self.friendly_name


class Question(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='')
    
    question = models.CharField(max_length=600)
    answer = models.TextField()

    def __str__(self):
        return self.question

    

