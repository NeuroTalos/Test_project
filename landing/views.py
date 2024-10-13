from django.shortcuts import render
from .forms import SubscriberFrom

# Create your views here.
def text(request):
    form = SubscriberFrom(request.POST or None)
    if request.method == "POST" and form.is_valid():
        #print(form.cleaned_data)

        new_form = form.save()
    return render(request, "landing.html", locals())