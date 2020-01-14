from django.shortcuts import render, redirect

def landing_page(request):

    if request.user.is_authenticated:
        return redirect('user_home_page_view')

    template = 'pages/landing_page.html'
    context = {}
    return render(request, template, context)