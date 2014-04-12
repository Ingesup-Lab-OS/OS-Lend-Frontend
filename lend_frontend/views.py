from django.shortcuts import render
from .lend_form import LendForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LendForm(request.POST)
    else:
        form = LendForm()

    return render(request, 'index.html', {
        'form': form,
    })