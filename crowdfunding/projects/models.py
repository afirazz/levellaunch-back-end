from django.db import models
from django.contrib.auth import get_user_model


class Project(models.Model):
    GAME_TYPE_CHOICES = {
        "video": "Video Game",
        "tabletop": "Tabletop Game",
        "mobile": "Mobile Game",
        "cards": "Playing Cards",
    }

    title = models.CharField(max_length=200)
    description = models.TextField()
    game_type = models.CharField(max_length=20, choices=GAME_TYPE_CHOICES)
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
    )


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_pledges'
    )