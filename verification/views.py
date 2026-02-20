from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from django.utils import timezone


from .models import Verification, VerificationImage
from .serializers import (
    VerificationSerializer,
    SubmitReportSerializer,
)

from .permissions import IsAdminOrAssignedAgent

class VerificationViewSet(viewsets.ModelViewSet):
    queryset = Verification.objects.select_related(
        "apartment",
        "assigned_agent"
    ).prefetch_related("images")

    serializer_class = VerificationSerializer
    permission_class = [IsAdminOrAssignedAgent]

    def get_queryset(self):
        user = self.request.user

        #admin sees all
        if user.is_admin:
            return self.queryset

        #agent sees only assigned tasks
        return self.queryset.filter(assigned_agent=user)

    #submit report endpoint
    @action(detail=True, methods=["post"],url_path="submit-report")
    def submit_report(self,request, pk=None):

        verification = self.get_object()

        serializer = SubmitReportSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)

        data = serializer.validated_data

        with transaction.atomic():
            verification.report = data["report"]
            verification.status = data["status"]
            verification.verification_date = timezone.now()
            verification.save()

            #update apartment status
            apartment = verification.apartment
            apartment.verification_status = data["status"]
            apartment.save(update_fields = ["verification_status"])

            #save images
            for image in data.get("images", []):
                VerificationImage.objects.create(
                    verification = verification,
                    image = image
                )

            return Response(
                {"detail": "Verification report submitted successfully."},
                status = status.HTTP_200_OK
            )
        
    #report retrieval endpoint
    @action(detail = True, methods = ["get"], url_path="report")
    def get_report(self, request, pk=None):
        verification = self.get_object()
        serializer = self.get_serializer(verification)
        return Response(serializer.data)