from django.shortcuts import render, redirect, get_object_or_404
from account.forms import GroupForm, CardSelectForm
from account.models import Group, CreditCard


def overview(request):
    groups = request.user.groups()
    return render(request,'account/groups/overview.html',{"groups" : groups})


def detailedview(request, pk):
    group = get_object_or_404(Group, pk=pk)

    return render(request,'account/groups/detailedview.html', {
        "group" : group,
    })


def participate(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = CardSelectForm(request.POST, user=request.user)
        if form.is_valid():
            id = form.cleaned_data['card']
            cc = CreditCard.objects.get(pk=id)
            group.cards.add(cc)
            group.save()
            return redirect('groups_overview')
    else:
        form = CardSelectForm(user=request.user)
    return render(request, 'account/groups/participate.html', {
        "group": group,
        "form": form
    })


def add(request):
    form = GroupForm()
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect('groups_participate', group.pk)
    else:
        form = GroupForm()
    return render(request, 'account/groups/group_add.html', {'form': form})
