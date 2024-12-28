from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSignUpSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomerLoginSerializer

class CustomerSignUpAPIView(APIView):
    def post(self, request):
        serializer = CustomerSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerLoginAPIView(APIView):
    def post(self, request):
        serializer = CustomerLoginSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.validated_data['customer']
            refresh = RefreshToken.for_user(customer)  # Generates JWT tokens
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': customer.username
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

