from django.shortcuts import render
from django.http import HttpResponseNotFound
from sentry_sdk import capture_message


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus.
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in.
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    return render(request, 'index.html')


def error_404(request, exception):
    """ Custom 404 error for handling by sentry """
    capture_message("Page not found!", level="error")

    # return any response here, e.g.:
    return HttpResponseNotFound("Not found")
