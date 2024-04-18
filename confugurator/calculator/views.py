from django.http.response import HttpResponse, JsonResponse
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
        try:
            price = request.query_params["cost"]
            category = int(request.query_params["category"])
            configuration = ConfigurationCreator(price, category).configuration
            serialized_configuration = ConfigurationSerializer(configuration).data
        except:
            return JsonResponse(
                {"message": "На такую цену пока ничего не собрать :("}, status=400
            )
        return JsonResponse(dict(serialized_configuration))


class CategoryListCreateView(ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategorySingleView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GPUListCreateView(ListCreateAPIView):

    queryset = GPU.objects.all()
    serializer_class = GPUSerializer


class CPUListCreateView(ListCreateAPIView):

    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


class MotherBoardListCreateView(ListCreateAPIView):

    queryset = MotherBoard.objects.all()
    serializer_class = MotherBoardSerializer


class RAMListCreateView(ListCreateAPIView):

    queryset = RAM.objects.all()
    serializer_class = RAMSerializer


class PowerUnitListCreateView(ListCreateAPIView):

    queryset = PowerUnit.objects.all()
    serializer_class = PowerUnitSerializer


### Special Creators


class MultyCreateView(GenericAPIView):
    model = None

    def post(self, request):
        data = request.data
        with transaction.atomic():
            for obj in data:
                self.model.objects.create(**obj)

        return HttpResponse("ok")


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
