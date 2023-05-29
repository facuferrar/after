from django.shortcuts import render
from .forms import MyForm
from .models import Modelo1, Modelo2, Modelo3, Modelo4

def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            modelo1 = Modelo1.objects.create(campo1=datos['campo1'], campo2=datos['campo2'])
            modelo2 = Modelo2.objects.create(campo3=datos['campo3'], campo4=datos['campo4'])
            modelo3 = Modelo3.objects.create(campo5=datos['campo5'], campo6=datos['campo6'])
            modelo4 = Modelo4.objects.create(campo7=datos['campo7'], campo8=datos['campo8'])
            # Realiza cualquier otra operación necesaria
            return render(request, 'miapp/exito.html')
    else:
        form = MyForm()
    return render(request, 'miapp/index.html', {'form': form})


