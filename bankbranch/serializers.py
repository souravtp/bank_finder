from rest_framework import serializers

from .models import Branches, BankBranch


class BranchSerializer(serializers.ModelSerializer):
    ifsc = serializers.CharField(required=True)

    class Meta:
        model = Branches
        fields = '__all__'


class BankBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankBranch
        fields = '__all__'
