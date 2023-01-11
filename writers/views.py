from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/signin/')
def writers_home_page(request):
    return render(request, 'writers/writers_home_page.html')
