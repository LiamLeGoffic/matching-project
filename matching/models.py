from django.db import models

# Create your models here.


class Skill(models.Model):
    description = models.CharField(max_length=100)
    #urlLogo ??

    def __str__(self):
        return f'{self.description}'


class Consultant(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    in_intercontrat = models.BooleanField(default=True)

    skills = models.ManyToManyField(Skill)     # un consultant est associé à différentes cométences

    def __str__(self):
        return f'Consultant : {self.email}'


class User(models.Model):

    class Role(models.TextChoices):
        RESSOURCE_MANAGER = 'RM'
        HUMAN_RESSOURCE = 'RH'
        COMMERCIAL = 'Com'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    office = models.CharField(max_length=10)
    role = models.CharField(choices=Role.choices, max_length=5)

    def __str__(self):
        return f'Utilisateur : {self.email}'


class Mission(models.Model):
    description = models.CharField(max_length=100, null=True)
    client = models.CharField(max_length=100)

    skills = models.ManyToManyField(Skill, through='Requirement')     # une mission est liée à plusieurs compétences
    writer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) # une mission peut avoir un auteur qui est un commercialou bien un Ressource Manager

    def __str__(self):
        return f'{self.writer.email} : {self.client}'
    

class Requirement(models.Model):

    class Level(models.TextChoices):
        BASIC = 1
        INTERMEDIATE = 2
        EXPERT = 3

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    level = models.IntegerField(choices=Level.choices)     # une mission requiert un certain niveau pour chaque compétence (importance de chaque compétence dans la mission)
