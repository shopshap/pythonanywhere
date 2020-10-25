from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=300)
    desc = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.img} '

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
