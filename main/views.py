from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Revaldy Hafizhy Mukhtar',
        'app_name': 'Backpack Inventory',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)
