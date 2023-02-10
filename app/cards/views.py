from django.contrib import messages
from django.shortcuts import render, redirect

from cards.models import Card, History


# При нажатии на кнопку активации обновлять время(создания)
def index_page(request):
    template_name = 'index.html'
    # Search
    search_query = request.GET.get('search', '')
    if search_query:
        cards_list = Card.objects.filter(name__icontains=search_query)
    else:
        cards_list = Card.objects.all()

    context = {'cards': cards_list}
    # Delete, activate cards
    if request.method == 'POST':
        if 'card-activate' in request.POST:
            obj_id = request.POST.get('card-activate')
            # Update the database
            Card.objects.filter(pk=int(obj_id)).update(activation=True)
            messages.success(request, "Card has been activated")
        elif 'card-delete' in request.POST:
            obj_id = request.POST.get('card-delete')
            Card.objects.filter(pk=int(obj_id)).delete()
            messages.success(request, "Card has been deleted")
        elif 'card-use' in request.POST:
            obj_id = request.POST.get('card-use')
            obj = Card.objects.get(pk=int(obj_id))
            History.objects.create(user=request.user, series=obj.series)
            Card.objects.filter(pk=int(obj_id)).delete()
        return redirect('/')

    return render(request, template_name, context)


def history_page(request):
    all_list = History.objects.all()
    context = {'history': all_list}
    return render(request, 'history.html', context)

