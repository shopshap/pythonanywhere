from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'

class Thaistory(models.Model): #เรื่องไทย
    thaistory_text = models.CharField(max_length=200) #ไทย

    def __str__(self):
        return f'{self.question_text}'

class CountryStory(models.Model):#ต่างจังหวัด
    story_type = models.ForeignKey(Thaistory, on_delete=models.CASCADE) #หมวดเรื่อง
    storyname = models.CharField(max_length=200) #ชื่อเรื่อง
    credit = models.CharField(max_length=200) #เครดิต

    def __str__(self):
        return f'{self.story_type}'

class requst(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    requststory = models.TextField()

    def __str__(self):
        return self.name