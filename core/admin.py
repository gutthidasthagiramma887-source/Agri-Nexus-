from django.contrib import admin
from .models import (
    FarmerProfile,
    Crop,
    Farm,
    CropCultivation,
    MarketPrice,
    Produce,
    DiseaseDetection,
    Advisory,
    WeatherData,
)


@admin.register(FarmerProfile)
class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone",
        "village",
        "district",
        "state",
        "land_area",
    )
    search_fields = (
        "user__username",
        "village",
        "district",
        "state",
    )


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "scientific_name",
        "season",
        "water_requirement",
        "soil_type",
    )
    search_fields = ("name", "scientific_name")
    list_filter = ("season",)


@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = (
        "farm_name",
        "farmer",
        "location",
        "area",
        "soil_type",
        "irrigation_type",
    )
    search_fields = (
        "farm_name",
        "location",
    )


@admin.register(CropCultivation)
class CropCultivationAdmin(admin.ModelAdmin):
    list_display = (
        "farm",
        "crop",
        "sowing_date",
        "expected_harvest_date",
        "area",
        "status",
    )
    list_filter = ("status",)


@admin.register(MarketPrice)
class MarketPriceAdmin(admin.ModelAdmin):
    list_display = (
        "crop",
        "market_name",
        "district",
        "minimum_price",
        "maximum_price",
        "modal_price",
        "price_date",
    )
    list_filter = ("district", "price_date")
    search_fields = (
        "market_name",
        "district",
        "crop__name",
    )


@admin.register(Produce)
class ProduceAdmin(admin.ModelAdmin):
    list_display = (
        "farmer",
        "crop",
        "quantity",
        "quality",
        "harvest_date",
        "expected_price",
        "available_for_sale",
    )
    list_filter = (
        "quality",
        "available_for_sale",
        "harvest_date",
    )
    search_fields = (
        "farmer__user__username",
        "crop__name",
    )


@admin.register(DiseaseDetection)
class DiseaseDetectionAdmin(admin.ModelAdmin):
    list_display = (
        "farmer",
        "crop",
        "detected_disease",
        "confidence",
        "detected_at",
    )
    list_filter = ("crop", "detected_disease")
    search_fields = (
        "farmer__user__username",
        "crop__name",
        "detected_disease",
    )


@admin.register(Advisory)
class AdvisoryAdmin(admin.ModelAdmin):
    list_display = (
        "crop",
        "title",
        "priority",
        "active",
        "created_at",
    )
    list_filter = (
        "priority",
        "active",
    )
    search_fields = (
        "title",
        "message",
    )


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = (
        "district",
        "temperature",
        "humidity",
        "rainfall",
        "wind_speed",
        "recorded_at",
    )
    list_filter = ("district",)