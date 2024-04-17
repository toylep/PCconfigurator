from rest_framework.serializers import ModelSerializer
from calculator.models import (
    GPU,
    CPU,
    MotherBoard,
    RAM,
    PowerUnit,
    Category,
    Configuration,
)


class GPUSerializer(ModelSerializer):
    class Meta:
        model = GPU
        fields = "__all__"


class CPUSerializer(ModelSerializer):
    class Meta:
        model = CPU
        fields = "__all__"


class MotherBoardSerializer(ModelSerializer):
    class Meta:
        model = MotherBoard
        fields = "__all__"


class RAMSerializer(ModelSerializer):
    class Meta:
        model = RAM
        fields = "__all__"


class PowerUnitSerializer(ModelSerializer):
    class Meta:
        model = PowerUnit
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ConfigurationSerializer(ModelSerializer):
    cpu = CPUSerializer()
    gpu = GPUSerializer()
    motherboard = MotherBoardSerializer()
    ram = RAMSerializer()
    power_unit = PowerUnitSerializer()

    class Meta:
        model = Configuration
        fields = "__all__"
