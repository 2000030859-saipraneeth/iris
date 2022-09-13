from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse



def home(request):
    return render(request, 'home.html')
# def result(request):
#     data={"dataset":PredResults.objects.all}
#     return render(request, 'result.html',data)
def predect(request):
    if request.method == "POST":
        sepal_length =request.POST.get('sepal_length')
        sepal_width = request.POST.get('sepa_width')
        petal_length = (request.POST.get('petal_length'))
        petal_width = (request.POST.get('petal_width'))
        print(sepal_length)
        # sepal_length = float(input("Enter sepal_length: "))
        # sepal_width = float(input("Enter sepa_width: "))
        # petal_length = float(input("Enter petal_length: "))
        # petal_width = float(input("Enter petal_width: "))

        model=pd.read_pickle(r"D:\iris\Irisproject\varna\varnaapp\new_model.pickle")
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        print(result[0])
        classification =result[0]

        return render(request,'result.html',{'result':classification})



