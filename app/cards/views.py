from django.contrib import messages
from django.shortcuts import render, redirect

from cards.models import Card


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
        return redirect('/')

    return render(request, template_name, context)



