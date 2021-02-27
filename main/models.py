from django.db import models

# Create your models here.
class WebsiteModel(models.Model):
    url = models.URLField()
    score = models.FloatField()
    raw_data = models.JSONField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            self.url
            + " | "
            + str(round(self.score, 3))
            + " | "
            + self.creation_date.strftime("%d/%m/%Y | %H:%M")
        )


class FailedWebsiteModel(models.Model):
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    error_message = models.TextField()

    def __str__(self):
        return self.url + " | " + self.creation_date.strftime("%d/%m/%Y | %H:%M")
