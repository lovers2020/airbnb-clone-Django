from django.urls import path
from experiences.views import (
    ExperienceBookings,
    ExperiencePerks,
    Experiences,
    ExperienceDetail,
    PerkDetail,
    Perks,
)


urlpatterns = [
    path("", Experiences.as_view()),
    path("<int:pk>", ExperienceDetail.as_view()),
    path("<int:pk>/perks", ExperiencePerks.as_view()),
    path("<int:pk>/bookings", ExperienceBookings.as_view()),
    path("perks", Perks.as_view()),
    path("perks/<int:pk>", PerkDetail.as_view()),
]
