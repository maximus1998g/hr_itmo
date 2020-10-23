from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from company.models import Company
from token_auth.enums import *


class CompanyListView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            if self.request.user.type != Type.EMPLOYER.value:
                return Response({'error': 'student can not create companies'}, status=status.HTTP_406_NOT_ACCEPTABLE)

            city = City.objects.filter(id=request.data.get('city'))
            if not city:
                return Response({'error': 'city does not exists'}, status=status.HTTP_404_NOT_FOUND)

            serializer.save(hr=self.request.user, city=city[0])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Company.objects.all().delete()
        return Response(status=status.HTTP_200_OK)