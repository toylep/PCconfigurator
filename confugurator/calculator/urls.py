from django.urls import path, include
from calculator.views import (
    CalculatorView,
    CPUListCreateView,
    GPUListCreateView,
    MotherBoardListCreateView,
    RAMListCreateView,
    PowerUnitListCreateView,
    MultyCPUCreateView,
    MultyGPUCreateView,
    MultyMotherBoardCreateView,
    MultyRAMCreateView,
    MultyPowerUnitCreateView,
    CategoryListCreateView,
)

urlpatterns = [
    path("cofiguration/new", CalculatorView.as_view()),
    path("category", CategoryListCreateView.as_view()),
    path("cpu", CPUListCreateView.as_view()),
    path("gpu", GPUListCreateView.as_view()),
    path("motherboard", MotherBoardListCreateView.as_view()),
    path("ram", RAMListCreateView.as_view()),
    path("powerunit", PowerUnitListCreateView.as_view()),
    path("multy/cpu", MultyCPUCreateView.as_view()),
    path("multy/gpu", MultyGPUCreateView.as_view()),
    path("multy/motherboard", MultyMotherBoardCreateView.as_view()),
    path("multy/ram", MultyRAMCreateView.as_view()),
    path("multy/powerunit", MultyPowerUnitCreateView.as_view()),
]
