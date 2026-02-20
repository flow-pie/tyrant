from django.core.exceptions import PermissionDenied
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
    permission_classes = [IsAdminOrAssignedAgent]
    serializer_class = VerificationSerializer

    def get_queryset(self):
        qs = Verification.objects.select_related(
            "apartment", "assigned_agent"
        ).prefetch_related("images")

        user = self.request.user
        if user.is_staff or getattr(user, 'is_admin', False):
            return qs
        return qs.filter(assigned_agent=user)

    @action(detail=True, methods=["post"], url_path="submit-report")
    def submit_report(self, request, pk=None):
        verification = self.get_object()

        #Prevent re-submission
        if verification.status == 'COMPLETED':
            return Response({"detail": "Report already submitted."}, status=400)

        serializer = SubmitReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        with transaction.atomic():
            verification.report = data["report"]
            verification.status = data["status"]
            verification.verification_date = timezone.now()
            verification.save()

            apartment = verification.apartment
            apartment.verification_status = data["status"]
            apartment.save(update_fields=["verification_status"])

            # Bulk create images
            images_to_create = [
                VerificationImage(verification=verification, image=img)
                for img in data.get("images", [])
            ]
            VerificationImage.objects.bulk_create(images_to_create)

        return Response(
            {"detail": "Verification report submitted successfully."},
            status=status.HTTP_200_OK
        )

    def perform_update(self, serializer):
        # Fix: use self.request.user
        if not self.request.user.is_admin:
            raise PermissionDenied("Only admins can modify verification records.")
        serializer.save()
