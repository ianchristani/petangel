from django.db import models
from django.contrib.auth.models import User

# the table
class EventModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50, blank = False, null = False)
    event = models.TextField(max_length = 250, blank = False, null = False)

    # pet's characteristics Session
    petsCharacteristics_eyes = (
        ("Yellow/Golden", "Yellow/Golden"),
        ("Green", "Green"),
        ("Blue", "Blue"),
        ("Copper/amber", "Copper/Amber"),
        ("Odd-Eyed", "Odd-Eyed (2 different colors each)"),
        ("Mixed Colors", "Mixed Colors")
    )
    eyesColor = models.CharField(max_length = 35, choices = petsCharacteristics_eyes, blank = True, null = True)

    petsCharacteristics_fur = (
        ("Black", "Black"),
        ("White", "White"),
        ("Orange", "Orange"),
        ("Grey", "Grey"),
        ("2 different colors", "2 different colors"),
        ("3 different colors", "3 different colors")
    )
    furColor = models.CharField(max_length = 18, choices = petsCharacteristics_fur, help_text="(The dominant one.)")

    petsCharacteristics_gender = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    gender = models.CharField(max_length = 6, choices = petsCharacteristics_gender, blank = True, null = True)

    petsCharacteristics_age = (
        ("baby (until 1 year old)", "baby (until 1 year old)"),
        ("adult (until 10 years old)", "adult (until 10 years old)"),
        ("senior (from 10 years old)", "senior (from 10 years old)")
    )
    age = models.CharField(max_length = 26, choices = petsCharacteristics_age, blank = True, null = True)

    # krakow's neighborhood
    locationOptions = (
            ("Bieńczyce", "Bieńczyce"),
            ("Bieżanów-Prokocim", "Bieżanów-Prokocim"),
            ("Bronowice", "Bronowice"),
            ("Czyżyny", "Czyżyny"),
            ("Dębniki", "Dębniki"),
            ("Grzegórzki", "Grzegórzki"),
            ("Krowodrza", "Krowodrza"),
            ("Łagiewniki–Borek Fałęcki", "Łagiewniki–Borek Fałęcki"),
            ("Mistrzejowice", "Mistrzejowice"),
            ("Nowa Huta", "Nowa Huta"),
            ("Podgórze", "Podgórze",),
            ("Podgórze Duchackie", "Podgórze Duchackie"),
            ("Prądnik Biały", "Prądnik Biały"),
            ("Prądnik Czerwony", "Prądnik Czerwony"),
            ("Stare Miasto", "Stare Miasto"),
            ("Swoszowice", "Swoszowice"), 
            ("Wzgórza Krzesławickie", "Wzgórza Krzesławickie"),
            ("Zwierzyniec", "Zwierzyniec")
        )

    # include the microship (blank = True)

    neighborhood = models.CharField(max_length = 25, choices = locationOptions, help_text="(The last time the pet was seen.)")
    contact = models.EmailField(blank = True, default = "youremail@example.com", help_text="(This info will be displayed only in the Pet Searcher, if the system finds potential candidates.)")
    pic  = models.ImageField(null = True, blank=True, upload_to = "media/")
    date = models.DateField(auto_now = True)

    # if the pet is lost is True
    lost = models.BooleanField(help_text = "(Mark this field if YOUR pet is LOST. If you found a pet DO NOT mark it.)")
    # this option is to be marked if the pet was found
    found = models.BooleanField(default = False, help_text="(Mark this field if your pet was FOUND)")

    # displaying the colunms with names
    def __str__(self) -> str:
        return f"title: {self.title}, author: {self.author}, event: {self.event}, neighborhood: {self.neighborhood}, date:{self.date}, lost:{self.lost}, found:{self.found}"
