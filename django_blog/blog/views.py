from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout as django_logout
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# -------------------
#    Home Page
# -------------------
def home(request):
    return render(request, 'blog/home.html')


# -------------------
#   Register View
# -------------------
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل الدخول مباشرة بعد التسجيل
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "auth/register.html", {"form": form})


# -------------------
#   Login View
# -------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})


# -------------------
#   Logout View
# -------------------
def logout_view(request):
    django_logout(request)
    return render(request, "auth/logout.html")


# -------------------
#   Profile View
# -------------------
@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "auth/profile.html", {"form": form})
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})
@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        new_email = request.POST.get("email")
        user.email = new_email
        user.save()
        return redirect("profile")

    return render(request, "profile.html", {"user": user})
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = "post_form.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
