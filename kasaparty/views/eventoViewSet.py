from rest_framework import viewsets
from kasaparty.models.evento import Evento
from kasaparty.serializers.eventoSerializer import EventoSerializer

from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    def perform_create(self, serializer):
        try:
            instance = serializer.save()

            # Verifica si hay un mensaje de validación
            if hasattr(instance, "mensaje_validacion") and instance.mensaje_validacion:
                mensaje_error = instance.mensaje_validacion
                return Response(
                    {"detail": mensaje_error}, status=status.HTTP_400_BAD_REQUEST
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as e:
            mensaje_error = str(e)
            return Response(
                {"detail": mensaje_error}, status=status.HTTP_400_BAD_REQUEST
            )
