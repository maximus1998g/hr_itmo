from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from .models import *
from .serializers import *
from .constants import *
from company.models import Company


class VacancyListView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)

        serializer_data = serializer.data
        for vacancy in serializer.data:
            vacancy['experience_type'] = {'id': vacancy.get('experience_type'),
                                          'text': Constants().get_employment_types(vacancy.get('experience_type'))}

            vacancy['employment_type'] = {'id': vacancy.get('employment_type'),
                                          'text': Constants().get_experience_types(vacancy.get('employment_type'))}

            vacancy['schedule_type'] = {'id': vacancy.get('schedule_type'),
                                        'text': Constants().get_schedule_types(vacancy.get('schedule_type'))}

        return Response(serializer_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            company = Company.objects.get(hr=self.request.user)
            if not company:
                return Response({'error': 'user does not belong to any company'}, status=status.HTTP_404_NOT_FOUND)

            serializer.save(company=company, skills=request.data.get('skills'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        Vacancy.objects.all().delete()
        return Response(status=status.HTTP_200_OK)


class SkillListView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestListView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, vacancy_id=request.data['vacancy'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        if self.request.user.type == Type.EMPLOYER.value:
            company = Company.objects.get(hr=self.request.user)
            requests = Request.objects.filter(company=company).order_by('created')
        elif self.request.user.type == Type.STUDENT.value:
            requests = Request.objects.filter(user=self.request.user).order_by('created')
        else:
            return Response({'': ''}, status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = RequestSerializer(instance=requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RespondRequestView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    @staticmethod
    def get_object(pk):
        try:
            return Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        request = self.get_object(pk)
        serializer = RequestSerializer(request, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
