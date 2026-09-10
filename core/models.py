from django.db import models
from django.contrib.auth.models import User


class FarmerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="farmer_profile"
    )

    phone = models.CharField(max_length=15, blank=True)
    village = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    state = models.CharField(
        max_length=100,
        default="Andhra Pradesh"
    )

    land_area = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Land area in acres"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Crop(models.Model):

    SEASON_CHOICES = [
        ("Kharif", "Kharif"),
        ("Rabi", "Rabi"),
        ("Zaid", "Zaid"),
        ("Year Round", "Year Round"),
    ]

    name = models.CharField(max_length=100)

    scientific_name = models.CharField(
        max_length=150,
        blank=True
    )

    season = models.CharField(
        max_length=30,
        choices=SEASON_CHOICES
    )

    water_requirement = models.CharField(
        max_length=100,
        blank=True
    )

    soil_type = models.CharField(
        max_length=150,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="crops/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Farm(models.Model):

    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE,
        related_name="farms"
    )

    farm_name = models.CharField(
        max_length=150
    )

    location = models.CharField(
        max_length=200
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    soil_type = models.CharField(
        max_length=100,
        blank=True
    )

    irrigation_type = models.CharField(
        max_length=100,
        blank=True
    )

    latitude = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitude = models.DecimalField(
        max_digits=10,
        decimal_places=6,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.farm_name


class CropCultivation(models.Model):

    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name="cultivations"
    )

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="cultivations"
    )

    sowing_date = models.DateField()

    expected_harvest_date = models.DateField(
        null=True,
        blank=True
    )

    area = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    expected_yield = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Expected yield in kg"
    )

    status = models.CharField(
        max_length=50,
        default="Growing"
    )

    def __str__(self):
        return f"{self.crop.name} - {self.farm.farm_name}"


class MarketPrice(models.Model):

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="market_prices"
    )

    market_name = models.CharField(
        max_length=150
    )

    district = models.CharField(
        max_length=100
    )

    minimum_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    maximum_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    modal_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    price_date = models.DateField()

    def __str__(self):
        return f"{self.crop.name} - {self.market_name}"


class Produce(models.Model):

    QUALITY_CHOICES = [
        ("A", "Grade A"),
        ("B", "Grade B"),
        ("C", "Grade C"),
    ]

    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE,
        related_name="produce"
    )

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="produce"
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Quantity in kg"
    )

    quality = models.CharField(
        max_length=1,
        choices=QUALITY_CHOICES
    )

    harvest_date = models.DateField()

    expected_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    available_for_sale = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.crop.name} - {self.quantity} kg"


class DiseaseDetection(models.Model):

    farmer = models.ForeignKey(
        FarmerProfile,
        on_delete=models.CASCADE,
        related_name="disease_detections"
    )

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="disease_detections"
    )

    image = models.ImageField(
        upload_to="disease_scans/"
    )

    detected_disease = models.CharField(
        max_length=200,
        blank=True
    )

    confidence = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )

    treatment = models.TextField(
        blank=True
    )

    detected_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.crop.name} - {self.detected_disease}"


class Advisory(models.Model):

    crop = models.ForeignKey(
        Crop,
        on_delete=models.CASCADE,
        related_name="advisories"
    )

    title = models.CharField(
        max_length=200
    )

    message = models.TextField()

    priority = models.CharField(
        max_length=20,
        default="Normal"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


class WeatherData(models.Model):

    district = models.CharField(
        max_length=100
    )

    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    humidity = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    rainfall = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    wind_speed = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    recorded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.district} - {self.recorded_at}"