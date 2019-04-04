from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

# Create your views here.
from .models import Neo

from .forms import NeoForm

def neo_create_view(request):
    # obj = Neo.objects.get(id=my_id)
    # obj = get_object_or_404(Neo, id=my_id)

    form = NeoForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NeoForm()

    context = {
        'form': form
    }
    return render(request, 'neo/neo_create.html', context)


def neo_create_id_view(request, my_id):
    # obj = Neo.objects.get(id=my_id)
    # obj = get_object_or_404(Neo, id=my_id)
    try:
        obj = Neo.objects.get(id=my_id)
    except Neo.DoesNotExist:
        raise Http404

    # form = NeoForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = NeoForm()

    context = {
        'object': obj
    }
    return render(request, 'neo/neo_create_id.html', context)


def neo_delete_id_view(request, my_id):
    obj = get_object_or_404(Neo, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    context = {
        'object': obj
    }
    return render(request, 'neo/neo_delete_id.html', context)


def neo_list_view(request):
    queryset = Neo.objects.all() # list of object
    context = {
        'object_list': queryset
    }
    return render(request, 'neo/neo_list.html', context)



