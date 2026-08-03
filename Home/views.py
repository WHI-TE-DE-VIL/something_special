from django.shortcuts import render

def home(request):
    return render(request, 'home_page.html')

# MAKE SURE THIS NEW VIEW IS EXACTLY HERE
def love_query(request):
    return render(request, 'love_query.html')

def memories(request):
    return render(request, 'memories.html')
def forever_vault(request):
    return render(request, 'final_vault.html')
def beginning(request):
    return render(request, 'beginning.html')
def ending(request):
    return render(request, 'ending.html')
def ending_page(request):
    # This renders the 5th final living letter celebration canvas
    return render(request, 'ending.html')