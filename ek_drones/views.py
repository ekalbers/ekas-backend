from django.core.mail import send_mail
from django.views.generic import CreateView
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import InfoRequest
from .serializer import InfoRequestSerializer
from .forms import InfoRequestForm
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt


class InfoRequestList(ListAPIView):
    queryset = InfoRequest.objects.all()
    serializer_class = InfoRequestSerializer


class InfoRequestDetail(RetrieveUpdateDestroyAPIView):
    queryset = InfoRequest.objects.all()
    serializer_class = InfoRequestSerializer

@csrf_exempt
class InfoRequestCreate(CreateView):
    model = InfoRequest
    form_class = InfoRequestForm
    success_url = 'success'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        company = form.cleaned_data['company']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        subject = f'{name} from {company}'
        message = f'email: {email}\nphone: {phone}\n\n{message}'
        from_email = 'inforequest@ekaerialsolutions.com'
        recipient_list = ['ethan@ekaerialsolutions.com']

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = 'success.html'
