from calculator.models import (
    GPU,
    CPU,
    MotherBoard,
    RAM,
    PowerUnit,
    Category,
    Configuration,
)


class ConfigurationCreator:

    def __init__(self, price: int, category_id: int):
        price_dict = self.divide_price(category_id, price)
        self.configuration = self.create_configuration(price_dict)

    def divide_price(self, category_id, price) -> dict[str, float]:
        # Находим категорию
        category = Category.objects.get(id=category_id)
        category_dict = category.__dict__
        # Очищаем все ненужное
        category_dict.pop("id")
        category_dict.pop("name")
        category_dict.pop("_state")
        # Высчитываем цены по коэффициентам
        all_coef = sum(category_dict.values())
        new_dict = {}
        for k, v in category_dict.items():
            if v != 0 & isinstance(v, float):
                v = float(price) * v / all_coef
                new_dict[k] = v
        return new_dict

    def create_configuration(self, price_dict: dict[str, float]) -> Configuration:
        # Получаем комплектующие в нужном порядке для совместимости
        if "gpu" in price_dict.keys() != 0:
            gpu = self.get_powerfull_gpu(price_dict["gpu"])
        else:
            gpu = None
        cpu = self.get_powerfull_cpu(price_dict["cpu"], gpu is None)
        print("cpu", cpu)
        # Если нужен GPU
        motherboard = self.get_powerfull_motherboard(price_dict["motherboard"], cpu)

        print("mb", motherboard)

        ram = self.get_powerfull_ram(price_dict["ram"], motherboard)
        print("ram", ram)
        max_tdp = (cpu.tdp + gpu.tdp if gpu is not None else 0) * 2 + 100
        power_unit = self.get_powerfull_powerunit(price_dict["power_unit"], max_tdp)
        print("bp", power_unit)

        return Configuration.objects.create(
            cpu=cpu, gpu=gpu, motherboard=motherboard, ram=ram, power_unit=power_unit
        )

    # Лямбда выражения для получения самого выгодного комплектующего
    get_powerfull_gpu = (
        lambda self, price: GPU.objects.filter(cost__lte=price).order_by("cost").last()
    )
    get_powerfull_cpu = (
        lambda self, price, is_graphics: CPU.objects.filter(
            cost__lte=price, is_graphics=is_graphics
        )
        .order_by("cost")
        .last()
    )
    get_powerfull_motherboard = (
        lambda self, price, cpu: MotherBoard.objects.filter(
            cost__lte=price, socket=cpu.socket
        )
        .order_by("cost")
        .last()
    )
    get_powerfull_ram = (
        lambda self, price, motherboard: RAM.objects.filter(
            cost__lte=price, type=motherboard.type_of_memory
        )
        .order_by("cost")
        .last()
    )
    get_powerfull_powerunit = (
        lambda self, price, max_tdp: PowerUnit.objects.filter(
            cost__lte=price, power__gte=max_tdp
        )
        .order_by("cost")
        .last()
    )
