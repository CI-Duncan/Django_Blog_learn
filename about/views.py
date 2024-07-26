from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_me(request):

    def about_me(request):
        """
        Renders the About page / the most recent info on the author
        and allows user collaboration requests
        Displays an individual instance of :model:`about.ABOUT`.
        **Context**
        ``about``
            The most recent instance of :model:`about.About`.
        ``collaborate_form``
            The most recent instance of :model:`about.CollaborateForm`.
        **Template**
            :template:`about/about.html`
        """
        about = About.objects.all().order_by('-updated_on').first()
        if request.method == "POST":
            collaborate_form = CollaborateForm(data=request.POST)
            if collaborate_form.is_valid():
                collaborate_form.save()
                messages.add_message(request, messages.SUCCESS, "Collaboration request received! I endeavour to respond within 2 working days.")

    
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )

