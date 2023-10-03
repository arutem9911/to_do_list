from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from to_do_list.models import Tasks, Project
from .forms import TaskModelForm, SearchForm, ProjectModelForm, ProjectTaskModelForm
from django.db.models import Q
from urllib.parse import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskIndexView(LoginRequiredMixin, ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    model = Tasks
    ordering = ['-created_at']
    paginate_by = 10
    paginate_orphans = 0
    page_kwarg = 'page'  # default 'page'

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if self.search_value:
            query = Q(description__icontains=self.search_value) | Q(short_description__icontains=self.search_value)
            qs = qs.filter(query)
        return qs

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')

    def get_search_form(self):
        return SearchForm(self.request.GET)


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/new_task.html'
    model = Tasks
    form_class = TaskModelForm

    def get_success_url(self):
        return reverse('detail_task', kwargs={'id': self.object.id})


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('all_tasks')
    template_name = 'delete.html'
    pk_url_kwarg = 'id'


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/update_task.html'
    form_class = TaskModelForm
    context_object_name = 'task'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('detail_task', kwargs={'id': self.object.id})


class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = 'tasks/detail_task.html'
    model = Tasks
    context_object_name = 'task'
    pk_url_kwarg = 'id'


class ProjectsIndexView(LoginRequiredMixin, ListView):
    template_name = 'projects/index.html'
    context_object_name = 'projects'
    model = Project
    ordering = ['end_date']
    paginate_by = 10
    paginate_orphans = 5
    page_kwarg = 'page'  # default 'page'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CreateProjectView(LoginRequiredMixin, CreateView):
    template_name = 'projects/create_project.html'
    model = Project
    form_class = ProjectModelForm

    def get_success_url(self):
        return reverse('detail_project', kwargs={'id': self.object.id})


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = 'projects/detail_project.html'
    model = Project
    context_object_name = 'project'
    pk_url_kwarg = 'id'
    extra_context = {'form': ProjectTaskModelForm}


class ProjectTaskCreateView(LoginRequiredMixin, CreateView):
    model = Tasks
    form_class = ProjectTaskModelForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, id=self.kwargs.get('id'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.project = self.project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail_project', kwargs={'id': self.project.id})


class UpdateProjectView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/update_project.html'
    form_class = ProjectModelForm
    context_object_name = 'project'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('detail_project', kwargs={'id': self.object.id})


class DeleteProjectView(LoginRequiredMixin, DeleteView):
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('all_projects')
    template_name = 'delete_project.html'
    pk_url_kwarg = 'id'
