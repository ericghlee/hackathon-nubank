from django.shortcuts import render


def overview(request):
    return render(request,'account/groups/overview.html',{})

def detailedview(request):
    return render(request,'account/groups/detailedview.html', {})

