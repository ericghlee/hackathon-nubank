from django.shortcuts import render, redirect
from account.forms import GroupForm
from account.models import Group

def overview(request):
    groups = Group.objects.filter(cards__in=request.user.creditcard_set.all())
    return render(request,'account/groups/overview.html',{"groups" : groups})

def detailedview(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request,'account/groups/detailedview.html', {"group" : group})

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
