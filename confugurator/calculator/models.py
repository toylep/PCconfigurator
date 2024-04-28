from django.db import models

# Create your models here.


class GPU(models.Model):
    """Видеокарта"""

    name = models.CharField(max_length=100)
    cost = models.FloatField()
    memory = models.IntegerField()
    bar = models.IntegerField()
    frequency = models.IntegerField(null=True)
    tdp = models.IntegerField()


class CPU(models.Model):
    """Процессор"""

    name = models.CharField(max_length=100)
    cost = models.FloatField()
    frequency = models.CharField(max_length=100, null=True)
    frequency_of_memory = models.IntegerField(null=True)
    tdp = models.IntegerField()
    socket = models.IntegerField()
    is_graphics = models.BooleanField()


class MotherBoard(models.Model):
    """Материнская плата"""

    name = models.CharField(max_length=100)
    cost = models.FloatField()
    socket = models.IntegerField()
    power_phases = models.IntegerField()
    type_of_memory = models.CharField(max_length=100)
    chipset = models.CharField(max_length=100)


class RAM(models.Model):
    """Оперативная память"""

    name = models.CharField(max_length=100)
    cost = models.FloatField()
    value_gb = models.IntegerField()
    type = models.CharField(max_length=100)
    frequency = models.IntegerField(null=True)
    is_game = models.BooleanField()
    count = models.IntegerField()


class PowerUnit(models.Model):
    """Блок питания"""

    name = models.CharField(max_length=100)
    cost = models.FloatField()
    power = models.IntegerField()


class Category(models.Model):
    """Категория ПК"""

    name = models.CharField(max_length=50)
    cpu = models.FloatField()
    gpu = models.FloatField()
    motherboard = models.FloatField()
    ram = models.FloatField()
    power_unit = models.FloatField()


class Configuration(models.Model):
    """Конфигурация ПК(Сборка)"""

    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE, null=True)
    motherboard = models.ForeignKey(MotherBoard, on_delete=models.CASCADE)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE)
    power_unit = models.ForeignKey(PowerUnit, on_delete=models.CASCADE)
