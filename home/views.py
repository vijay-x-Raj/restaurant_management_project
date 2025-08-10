from django.shortcuts import render


def error_404(request, exception):
    return render(request, 'home/error.html', status=404)