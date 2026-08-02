from django.shortcuts import render

def home(request):
    return render(request, 'home_page.html')

# MAKE SURE THIS NEW VIEW IS EXACTLY HERE
def love_query(request):
    return render(request, 'love_query.html')

def memories(request):
    return render(request, 'memories.html')
def final_vault(request):
    return render(request, 'final_vault.html')