from django.shortcuts import render

def show_main(request):
    context = {
        'app name': 'NBA Trading Cards',
        'name': 'Muhamad Pascal Alfin Pahlevi',
        'class': 'PBP International Class'
    }

    return render(request, 'main.html', context)