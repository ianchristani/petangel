from django.db import models
from django.contrib.auth.models import User

# the table
class EventModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50, blank = False, null = False)
    event = models.TextField(max_length = 250, blank = False, null = False)

    # krakow's neighborhood
    options = (
            ("bienczyce", "Bieńczyce"),
            ("prokocim", "Bieżanów-Prokocim"),
            ("bronowice", "Bronowice"),
            ("czyzyny", "Czyżyny"),
            ("debniki", "Dębniki"),
            ("grzegorzki", "Grzegórzki"),
            ("krowodrza", "Krowodrza"),
            ("lagiewniki_Borek", "Łagiewniki–Borek Fałęcki"),
            ("mistrzejowice", "Mistrzejowice"),
            ("nowahuta", "Nowa Huta"),
            ("podgorze", "Podgórze",),
            ("podgorze_duchackie", "Podgórze Duchackie"),
            ("pradnik_bialy", "Prądnik Biały"),
            ("pradnik_czerwony", "Prądnik Czerwony"),
            ("stare_miasto", "Stare Miasto"),
            ("swoszowice", "Swoszowice"), 
            ("wzgorza_krzeslawickie", "Wzgórza Krzesławickie"),
            ("zwierzyniec", "Zwierzyniec")
        )

    neighborhood = models.CharField(max_length = 25, choices = options, help_text="(The last time the pet was seen.)")
    pic  = models.ImageField(null = True, blank=True, upload_to = "media/")
    date = models.DateField(auto_now = True)
    # if the pet is lost is True
    lost = models.BooleanField(help_text = "(Mark this field if your pet is LOST. If you found a pet DO NOT mark it.)")
    # this option is to be marked if the pet was found
    found = models.BooleanField(default = False, help_text="(Mark this field if your pet was FOUND)")

    # displaying the colunms with names
    def __str__(self) -> str:
        return f"title: {self.title}, author: {self.author}, event: {self.event}, neighborhood: {self.neighborhood}, date:{self.date}, lost:{self.lost}, found:{self.found}"
