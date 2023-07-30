from django.core.mail import send_mail
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import InfoRequest
from .serializer import InfoRequestSerializer
from rest_framework.response import Response


class InfoRequestList(ListAPIView):
    queryset = InfoRequest.objects.all()
    serializer_class = InfoRequestSerializer


class InfoRequestDetail(RetrieveUpdateDestroyAPIView):
    queryset = InfoRequest.objects.all()
    serializer_class = InfoRequestSerializer


class InfoRequestCreateView(CreateAPIView):
    queryset = InfoRequest.objects.all()
    serializer_class = InfoRequestSerializer

    def perform_create(self, serializer):
        # Save the InfoRequest object
        instance = serializer.save()

        # Send an email with the new InfoRequest data
        subject = f'{instance.name} from {instance.company}'
        message = f'Email: {instance.email}\n' \
                  f'Phone: {instance.phone}\n' \
                  f'Message: {instance.message}'
        from_email = 'ethan@ekaerialsolutions.com'  # Replace this with your email address
        recipient_list = ['info@ekaerialsolutions.com']  # Replace this with your recipient email address(es)

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        # Optionally, you can also return a custom response after the object is created
        return Response(serializer.data, status=201)

