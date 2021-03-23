from django.shortcuts import render

def index(request):
    return render(request, 'serv/1.html')
def index1(request):
    remote_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    ip = remote_address
    user_info = request.META.get('HTTP_USER_AGENT')
    return render(request, 'serv/2.html', locals())
