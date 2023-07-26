from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Banks, Branches, BankBranch
from .serializers import BranchSerializer, BankBranchSerializer

# Create your views here.


class BanksList(ListView):
    model = Banks
    template_name = 'banks.html'
    context_object_name = 'banks'


class BankDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        ifsc = request.data.get('ifsc')

        try:
            bank = Branches.objects.get(ifsc=ifsc)
        except Branches.DoesNotExist:
            return Response({"error": "branch does not exists."})

        serializer = BranchSerializer(bank)

        return Response(serializer.data)


class BanksInCity(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        bank_name = request.data.get("bank_name")
        city = request.data.get("city")

        bank_branch = BankBranch.objects.filter(bank_name=bank_name, city=city)

        if not bank_branch:
            return Response({"error": "banks not found"})

        serializer = BankBranchSerializer(bank_branch, many=True)

        return Response(serializer.data)
