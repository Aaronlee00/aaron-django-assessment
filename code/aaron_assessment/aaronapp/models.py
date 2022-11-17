from django.db import models

class Data(models.Model):
    user_ID = models.CharField(max_length=80)
    keyin = models.IntegerField()
    input = 3
    score = input + 1

    def keyin_total_score(self):
         result = self.keyin + 1
         return result




