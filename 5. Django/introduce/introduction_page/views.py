from django.shortcuts import render

# Create your views here.
def mypage_view(request):
    return render(request, 'my_page.html', {})