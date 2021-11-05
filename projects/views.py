from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView

from .models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projects/project_list.html'
    login_url = 'account_login'


class ProjectDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'
    login_url = 'account_login'
    permission_required = 'projects.special_status'


class SearchResultsListView(ListView):
    model = Project
    context_object_name = 'search_results'
    template_name = 'projects/search_results.html'

