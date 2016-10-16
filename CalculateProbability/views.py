from django.shortcuts import render
from models import InputForm
from compute import compute
# Create your views here.
def post_answer(request):
    #assign default value of result
    result = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(form2.Numsides)

    else:
        form = InputForm()

    #render the page
    return render(request,'CalculateProbability/post_answer.html',
            {'form': form,
             'result': result,
             })