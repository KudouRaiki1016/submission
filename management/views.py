from django.shortcuts import render

def top_view(request):
    context = {}
    return render(request, 'management/top_page.html', context)
