from django.db import models

class Faq(models.Model):

    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject




class Question(models.Model):

    subject = models.ForeignKey(Faq, on_delete=models.CASCADE, default='')
    question = models.CharField(max_length=600)
    answer = models.TextField()

    def __str__(self):
        return self.question

