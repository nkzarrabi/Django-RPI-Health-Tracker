from django.db import models

class SleepData(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    deep_sleep_duration = models.DurationField()
    light_sleep_duration = models.DurationField()
    sleep_score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Sleep from {self.start_time} to {self.end_time} with score {self.sleep_score}"


class SleepwalkingEvent(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    #duration = models.IntegerField(blank=True, null=True)
    intensity = models.CharField(max_length=255)  # or use another appropriate field type
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Sleepwalking from {self.start_time} to {self.end_time}, Intensity: {self.intensity}"