from django.shortcuts import render


def post_list(request):
    return render(request, 'blog.html\post_list.html', {})
