
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
# Question Model
# Question and Publication date
# Question and Publication Date = Column Names
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
# Choice Model
# text of choice and vote tally
# each choice is associated with a vote
# choice_text and votes = column names
# Foreign Key = relationship between Choice and Question, each choice is associated with one ?
    def __str__(self):
        return self.choice_text
