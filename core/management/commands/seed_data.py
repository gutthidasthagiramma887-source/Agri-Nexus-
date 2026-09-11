from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import (
    FarmerProfile, Farm, Crop, CropCultivation,
    MarketPrice, Produce, Advisory
)
from datetime import date


class Command(BaseCommand):
    help = "Create demo data for Agri-Nexus"

    def handle(self, *args, **kwargs):

        # -----------------------------
        # FARMER
        # -----------------------------
        user, created = User.objects.get_or_create(
            username="Dasthagiramma"
        )

        if created:
            user.set_password("AgriNexus@123")
            user.save()

        profile, _ = FarmerProfile.objects.get_or_create(
            user=user,
            defaults={
                "phone": "9876543210",
                "village": "Orvakal",
                "district": "Kurnool",
                "state": "Andhra Pradesh",
                "land_area": 5,
            }
        )

        # -----------------------------
        # FARM
        # -----------------------------
        farm, _ = Farm.objects.get_or_create(
            farmer=profile,
            farm_name="Dasthagiramma Green Farm",
            defaults={
                "location": "Kurnool, Andhra Pradesh",
                "area": 5,
                "soil_type": "Black Soil",
                "irrigation_type": "Borewell",
                "latitude": 15.828100,
                "longitude": 78.035200,
            }
        )

        # -----------------------------
        # CROPS
        # -----------------------------
        crops_data = [
            ("Rice", "Oryza sativa", "Kharif", "High",
             "Clayey / Black Soil"),
            ("Wheat", "Triticum aestivum", "Rabi", "Medium",
             "Loamy Soil"),
            ("Cotton", "Gossypium", "Kharif", "Medium",
             "Black Soil"),
            ("Maize", "Zea mays", "Kharif", "Medium",
             "Loamy Soil"),
            ("Groundnut", "Arachis hypogaea", "Kharif", "Medium",
             "Sandy Loam"),
            ("Chilli", "Capsicum annuum", "Year Round", "Medium",
             "Well-drained fertile soil"),
            ("Mango", "Mangifera indica", "Year Round", "Medium",
             "Well-drained loamy soil"),
            ("Pomegranate", "Punica granatum", "Year Round", "Medium",
             "Well-drained loamy soil"),
            ("Guava", "Psidium guajava", "Year Round", "Medium",
             "Well-drained loamy soil"),
            ("Sapota", "Manilkara zapota", "Year Round", "Medium",
             "Well-drained sandy loam"),
        ]

        crop_objects = {}

        for name, scientific, season, water, soil in crops_data:
            crop, _ = Crop.objects.get_or_create(
                name=name,
                defaults={
                    "scientific_name": scientific,
                    "season": season,
                    "water_requirement": water,
                    "soil_type": soil,
                    "description": f"{name} crop management and smart farming information.",
                }
            )
            crop_objects[name] = crop

        # -----------------------------
        # CULTIVATION
        # -----------------------------
        rice = crop_objects["Rice"]

        CropCultivation.objects.get_or_create(
            farm=farm,
            crop=rice,
            defaults={
                "sowing_date": date(2026, 8, 1),
                "expected_harvest_date": date(2026, 12, 1),
                "area": 4,
                "expected_yield": 8000,
                "status": "Growing",
            }
        )

        # -----------------------------
        # MARKET PRICE
        # -----------------------------
        MarketPrice.objects.get_or_create(
            crop=rice,
            market_name="Kurnool Agricultural Market",
            price_date=date(2026, 9, 10),
            defaults={
                "district": "Kurnool",
                "minimum_price": 2000,
                "maximum_price": 2500,
                "modal_price": 2300,
            }
        )

        # -----------------------------
        # PRODUCE
        # -----------------------------
        Produce.objects.get_or_create(
            farmer=profile,
            crop=rice,
            harvest_date=date(2026, 9, 10),
            defaults={
                "quantity": 1000,
                "quality": "A",
                "expected_price": 2300,
                "available_for_sale": True,
            }
        )

        # -----------------------------
        # ADVISORY
        # -----------------------------
        Advisory.objects.get_or_create(
            crop=rice,
            title="Rice Crop Growth Advisory",
            defaults={
                "message": (
                    "Maintain proper irrigation, monitor leaf health "
                    "and regularly check for pest attacks."
                ),
                "priority": "High",
                "active": True,
            }
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Agri-Nexus demo data created successfully!"
            )
        )