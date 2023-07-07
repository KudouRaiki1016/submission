from django.shortcuts import render
from .models import Task

def top_view(request):
    object_list = Task.objects.order_by('-created_at')  # -(マイナス)をつけることで逆順(新規順)になる
    context = {'object_list': object_list}
    return render(request, 'management/top_page.html', context)
