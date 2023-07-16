# from django.http import HttpResponse, Http404
# from django.template import loader

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Album, Song
from .forms import UserForm

class IndexView(ListView):
    template_name = "music/index.html"
    context_object_name = "all_albums"

    def get_queryset(self):
        return Album.objects.all()
    
class DetailView(DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = "__all__"

class AlbumUpdate(UpdateView):
    model = Album
    fields = "__all__"

class AlbumDelete(DeleteView):
    model = Album
    fields = "__all__"
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalised) data // unifies data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns user objects if credentials are correct
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
            
        return render(request, self.template_name, {'form':form})