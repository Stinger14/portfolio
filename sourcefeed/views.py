from django.views.generic import ListView

from .models import PythonFeed, NbaFeed, RemoteJobsFeed, TechFeed


class PythonFeedView(ListView):
    template_name = 'sourcefeed/python_content.html'
    model = PythonFeed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sourcefeed'] = PythonFeed.objects.filter().order_by("-pub_date")[:10]
        return context

