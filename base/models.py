from django.db import models

# Create your models here.

DIVISION_CHOICES = (
   ("Dhaka",
     "Dhaka"),
    ("Chittagong",
     "Chittagong"),
    ("Khulna",
     "Khulna"),
    ("Rajshahi",
     "Rajshahi"),
    ("Barisal",
     "Barisal"),
    ("Sylhet",
     "Sylhet"),
    ("Rangpur",
     "Rangpur"),
     ("Mymensingh",
     "Mymensingh")
)

STATE_CHOICES = (
    ("Dhaka",
     "Dhaka"),
    ("Chittagong",
     "Chittagong"),
    ("Khulna",
     "Khulna"),
    ("Rajshahi",
     "Rajshahi"),
    ("Barisal",
     "Barisal"),
    ("Sylhet",
     "Sylhet"),
    ("Rangpur",
     "Rangpur"),
    ("Comilla",
     "Comilla"),
    ("Narayanganj",
     "Narayanganj"),
    ("Gazipur",
     "Gazipur"),
    ("Mymensingh",
     "Mymensingh"),
    ("Cox's Bazar",
     "Cox's Bazar"),
    ("Jessore",
     "Jessore"),
    ("Tangail",
     "Tangail"),
    ("Feni",
     "Feni"),
    ("Pabna",
     "Pabna"),
    ("Netrokona",
     "Netrokona"),
    ("Narail",
     "Narail"),
    ("Bogura",
     "Bogura"),
    ("Pirojpur",
     "Pirojpur"),

)



class Record(models.Model):
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   email = models.EmailField()
   phone = models.CharField(max_length=15)
   division =  models.CharField(max_length=100, choices=DIVISION_CHOICES,null=True)
   city =  models.CharField(max_length=50,choices=STATE_CHOICES,null=True)
   state =  models.CharField(max_length=50)
   zipcode =  models.CharField(max_length=20)
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
    return(f"{self.first_name} {self.last_name}")