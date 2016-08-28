from django.shortcuts import render, redirect
from account.forms import GroupForm


def overview(request):
    return render(request,'account/groups/overview.html',{})


def detailedview(request):
    return render(request,'account/groups/detailedview.html', {})


def add(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('groups_detailed', group.pk)
    else:
        form = GroupForm()
    return render(request, 'account/groups/group_add.html', {'form': form})