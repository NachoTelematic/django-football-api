from django.db import models

class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    logo = models.ImageField(
        upload_to="league/%Y/%m/", blank=True, null=True)
    
    def __str__(self):
        return u"%s - %s" % (self.name, self.country)

class Team(models.Model):
    name = models.CharField(max_length=200)
    stadium = models.CharField(max_length=200)
    league = models.ForeignKey(
        League, on_delete=models.CASCADE, related_name="leagues")

    def __str__(self):
        return u"%s" % (self.name,)

class Player(models.Model):
    POSITIONS = (('GK', 'Goalkeeper'), ('DF', 'Defender'),
                    ('MF', 'Midfield'), ('FW', 'Forward'),)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    age = models.IntegerField()
    height = models.IntegerField()
    place_birth = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITIONS)
    image = models.ImageField(upload_to="players", blank=True, null=True)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="teams")

    def __str__(self):
        return u"%s %s" % (self.first_name, self.last_name)

