from django.db import models

# Create your models here.
class idiom(models.Model):
    word = models.CharField(max_length=150, null=False, blank= False, unique=True)
    explaination = models.TextField(null=True, blank=True)
    chinese = models.CharField(max_length=150, default='', blank= False)

    def __str__(self) -> str:
        return self.word

class idiomSample(models.Model):
    idiom = models.ForeignKey(idiom, on_delete=models.CASCADE)
    sampleSentence = models.TextField(null=False, blank=False, verbose_name="sample sentense")

    def __str__(self) -> str:
        return self.idiom.word