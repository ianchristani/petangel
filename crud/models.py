from django.db import models
from django.contrib.auth.models import User

# the table
class EventModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField(max_length = 50, blank = False, null = False, verbose_name="Tytuł")
    event = models.TextField(max_length = 250, blank = False, null = False, verbose_name="Opis")
    
    # pet type 
    petType = (
        ("kot", "kot"),
        ("pies", "pies"),
        ("inny", "inny")
    )
    type = models.CharField(max_length = 5, blank = False, null = False, choices = petType, verbose_name="Typ zwierzaka")

    # pet's characteristics Session
    petsCharacteristics_eyes = (
        ("Żółty/złoty", "Żółty/złoty"),
        ("Zielony", "Zielony"),
        ("Niebieski", "Niebieski"),
        ("Miedź/bursztyn", "Miedź/bursztyn"),
        ("Dziwne oczy", "Dziwne oczy"),
        ("Mieszane kolory", "Mieszane kolory")
    )
    eyesColor = models.CharField(max_length = 35, choices = petsCharacteristics_eyes, blank = True, null = True, verbose_name="Kolor oczu")

    petsCharacteristics_fur = (
        ("Czarny", "Czarny"),
        ("Biały", "Biały"),
        ("Pomarańczy", "Pomarańczy"),
        ("Szary", "Szary"),
        ("Dwa różne kolory", "Dwa różne kolory"),
        ("Try różne kolory", "Try różne kolory")
    )
    furColor = models.CharField(max_length = 18, choices = petsCharacteristics_fur, help_text="(Dominujący)", verbose_name="Kolor futra")

    petsCharacteristics_gender = (
        ("Mężczyzna", "Mężczyzna"),
        ("Kobieta", "Kobieta")
    )
    gender = models.CharField(max_length = 9, choices = petsCharacteristics_gender, blank = True, null = True, verbose_name="Płeć")

    petsCharacteristics_age = (
        ("dziecko (do 1 roku życia)", "dziecko (do 1 roku życia)"),
        ("dorosły (do 10 roku życia)", "dorosły (do 10 roku życia)"),
        ("seniorzy (od 10 lat)", "seniorzy (od 10 lat)")
    )
    age = models.CharField(max_length = 26, choices = petsCharacteristics_age, blank = True, null = True, verbose_name="Wiek")

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

    neighborhood = models.CharField(max_length = 25, choices = locationOptions, help_text="(Ostatni raz widziano zwierzaka.)", verbose_name="Sąsiedztwo")
    contact = models.EmailField(blank = True, default = "youremail@example.com", help_text="(Informacja ta wyświetli się tylko w Wyszukiwarce Zwierzaków, jeśli system znajdzie potencjalnych kandydatów.)", verbose_name="Kontakt")
    pic  = models.ImageField(null = True, blank=True, upload_to = "media/", verbose_name="Zdjęcie")
    date = models.DateField(auto_now = True, verbose_name="Data")

    # if the pet is lost is True
    lost = models.BooleanField(help_text = "(Zaznacz to pole, jeśli TWÓJ zwierzak zaginął. Jeśli znalazłeś zwierzaka, NIE zaznaczaj go.)", verbose_name="Zaginął zwierzęta")
    # this option is to be marked if the pet was found
    found = models.BooleanField(default = False, help_text="(Zaznacz to pole, jeśli ZNALEZIONO Twoje zwierzę)", verbose_name="Znaleziono zwierzęta")

    # displaying the colunms with names
    def __str__(self) -> str:
        return f"title: {self.title}, author: {self.author}, event: {self.event}, neighborhood: {self.neighborhood}, date:{self.date}, lost:{self.lost}, found:{self.found}"
