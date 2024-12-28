from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from .models import Customer

class CustomerSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['username', 'password']

    def create(self, validated_data):
        # Create a new customer, the password will be hashed in the model's `save` method
        customer = Customer.objects.create(**validated_data)
        return customer

class CustomerLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        try:
            customer = Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password.")

        # Check if the password is valid
        if not check_password(password, customer.password):
            raise serializers.ValidationError("Invalid username or password.")

        data['customer'] = customer
        return data
