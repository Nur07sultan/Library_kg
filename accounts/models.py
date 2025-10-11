from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    middle_name = models.CharField("Отчество", max_length=150, blank=True)
    date_of_birth = models.DateField("Дата рождения", null=True, blank=True)
    phone_number = models.CharField("Телефон", max_length=20, blank=True)
    city = models.CharField("Город", max_length=100, blank=True)
    education = models.CharField("Образование", max_length=255, blank=True)
    position_applied = models.CharField("Должность", max_length=255, blank=True)
    experience_years = models.PositiveIntegerField("Опыт работы (лет)", default=0)
    github_link = models.URLField("GitHub", blank=True)
    portfolio_link = models.URLField("Портфолио", blank=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


