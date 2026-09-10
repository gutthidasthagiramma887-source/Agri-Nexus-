from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "register/",
        views.register,
        name="register"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "farms/",
        views.farms,
        name="farms"
    ),

    path(
        "crops/",
        views.crops,
        name="crops"
    ),

    path(
        "market/",
        views.market,
        name="market"
    ),

    path(
        "produce/",
        views.produce,
        name="produce"
    ),

    path(
        "disease/",
        views.disease_detection,
        name="disease_detection"
    ),

    path(
        "advisory/",
        views.advisory,
        name="advisory"
    ),

    path(
        "weather/",
        views.weather,
        name="weather"
    ),

    path(
        "profile/",
        views.profile,
        name="profile"
    ),

    path(
        "traceability/",
        views.traceability,
        name="traceability"
    ),

    path(
        "traceability/<int:produce_id>/",
        views.produce_traceability,
        name="produce_traceability"
    ),

    path("ai-advisory/", views.ai_advisory, name="ai_advisory"),
    path(
        "crop-recommendation/",
        views.crop_recommendation,
        name="crop_recommendation"
    ),
]