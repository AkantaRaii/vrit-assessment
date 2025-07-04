from rest_framework import serializers
from .models import ExpenseIncome

class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseIncome
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False}
        }

    def get_total(self, obj):
        return obj.total
