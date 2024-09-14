from django.shortcuts import render
import math

def view_calculator(request):
    num1 = float(request.POST.get('t1', 0))
    num2 = float(request.POST.get('t2', 0))
    result = None

    if request.method == 'POST':
        if 'btnsum' in request.POST:
            result = num1 + num2
        elif 'btnsub' in request.POST:
            result = num1 - num2
        elif 'btnmult' in request.POST:
            result = num1 * num2
        elif 'btndiv' in request.POST:
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        elif 'btnmod' in request.POST:
            result = num1 % num2
        elif 'btnpow' in request.POST:
            result = num1 ** num2
        elif 'btnsqrt' in request.POST:
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                result = "Error: Negative input for sqrt"
        
        context = {'num1': num1, 'num2': num2, 'result': result}
        return render(request, 'index.html', context)

    return render(request, 'index.html')