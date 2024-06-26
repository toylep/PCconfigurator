from django.http.response import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.generics import (
    ListCreateAPIView,
    GenericAPIView,
    RetrieveUpdateDestroyAPIView,
)
from calculator.creator import ConfigurationCreator
from calculator.serializers import (
    ConfigurationSerializer,
    CategorySerializer,
    CPUSerializer,
    GPUSerializer,
    MotherBoardSerializer,
    RAMSerializer,
    PowerUnitSerializer,
    ConfigOptionsSerializer,
)
from calculator.models import (
    Category,
    GPU,
    CPU,
    MotherBoard,
    RAM,
    PowerUnit,
    Configuration,
)
from django.db import transaction


@extend_schema(parameters=[ConfigOptionsSerializer], responses=ConfigurationSerializer)
class CalculatorView(GenericAPIView):
    queryset = Configuration.objects.all()

    def get(self, request):
        """Точка на генерацию конфигурации

        Returns:
            json : Сериализованная готовая сборка
        """
        try:
            price = request.query_params["cost"]
            category = request.query_params["category"]
            configuration = ConfigurationCreator(price, category).configuration
            serialized_configuration = ConfigurationSerializer(configuration).data
        except:
            return JsonResponse(
                {"message": "На такую цену пока ничего не собрать :("}, status=400
            )
        return JsonResponse(dict(serialized_configuration))


class CategoryListCreateView(ListCreateAPIView):
    """Создание/Получение списка категорий"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategorySingleView(RetrieveUpdateDestroyAPIView):
    """Изменение/удаление категории"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GPUListCreateView(ListCreateAPIView):
    """Получение/Добавление видеокарты"""

    queryset = GPU.objects.all()
    serializer_class = GPUSerializer


class CPUListCreateView(ListCreateAPIView):
    """Получение/добавление процессора"""

    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


class MotherBoardListCreateView(ListCreateAPIView):
    """Получение/добавление материнской платы"""

    queryset = MotherBoard.objects.all()
    serializer_class = MotherBoardSerializer


class RAMListCreateView(ListCreateAPIView):
    """Получение/добавление оперативной памяти"""

    queryset = RAM.objects.all()
    serializer_class = RAMSerializer


class PowerUnitListCreateView(ListCreateAPIView):
    """Получение/добавление блока питания"""

    queryset = PowerUnit.objects.all()
    serializer_class = PowerUnitSerializer


### Special Creators


class MultyCreateView(GenericAPIView):
    """Абстракция чтобы можно было добавлять обьекты сразу списками"""

    model = None

    def post(self, request):
        data = request.data
        with transaction.atomic():
            for obj in data:
                self.model.objects.create(**obj)

        return JsonResponse({"messgage": "ok"}, status=201)


class MultyCPUCreateView(MultyCreateView):
    model = CPU
    serializer_class = CPUSerializer
    queryset = CPU.objects.all()


class MultyGPUCreateView(MultyCreateView):
    model = GPU
    serializer_class = GPUSerializer
    queryset = GPU.objects.all()


class MultyMotherBoardCreateView(MultyCreateView):
    model = MotherBoard
    serializer_class = MotherBoardSerializer
    queryset = MotherBoard.objects.all()


class MultyRAMCreateView(MultyCreateView):
    model = RAM
    serializer_class = RAMSerializer
    queryset = RAM.objects.all()


class MultyPowerUnitCreateView(MultyCreateView):
    model = PowerUnit
    serializer_class = PowerUnitSerializer
    queryset = PowerUnit.objects.all()
