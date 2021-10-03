from rest_framework import serializers

from companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(required=True)

    class Meta:
        model = Company
        fields = ("company_name", "password")

    def validate_company_name(self, value):
        company = Company.objects.filter(company_name=value)
        if company:
            raise serializers.ValidationError("Company with this name already exists")
        return value
