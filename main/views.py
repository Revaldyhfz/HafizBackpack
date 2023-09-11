from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Pak Bepe',
        'app_name': 'Backpack Inventory',
        'class': 'PBP A'
    }

    return render(request, 'main.html', context)
