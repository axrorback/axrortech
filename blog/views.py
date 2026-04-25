from django.shortcuts import redirect
from django.views.generic import ListView , DetailView
from .models import Post , Comment

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_active=True)
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(
            is_active=True
        ).prefetch_related(
            'comments',
            'comments__user'
        )

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('post_list')

        self.object = self.get_object()

        text = request.POST.get("text")

        if text and text.strip():
            Comment.objects.create(
                post=self.object,
                user=request.user,
                text=text.strip()
            )

        return redirect(
            'post_detail',
            slug=self.object.slug
        )