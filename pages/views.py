from django.shortcuts import render

def landing_page(request):
    template = 'pages/landing_page.html'
    context = {}
    return render(request, template, context)