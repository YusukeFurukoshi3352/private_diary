from django.views import  generic

from .forms import InquiryForm

class IndexView(generic.TemplateView):
    template_name = "blog/index.html"

class InquiryView(generic.FormView):
    template_name = "blog/inquiry.html"
    form_class = InquiryForm