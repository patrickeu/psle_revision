from django.db import models

# Create your models here.
class word(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name
    
class wordMeaning(models.Model):
    word = models.ForeignKey(word, null=False, blank=False, on_delete=models.CASCADE)
    description = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return self.description
    
class sampleSentence(models.Model):
    meaning = models.ForeignKey(wordMeaning, on_delete=models.CASCADE)
    sentence = models.TextField()

    def word(self):
        return self.meaning.word

    def __str__(self) -> str:
        return self.sentence