from django.shortcuts import render

def calc_power(request):
    context = {}
    context['p'] = "0"
    context['i'] = "0"
    context['r'] = "0"

    if request.method == 'POST':
        print("POST method is used")
        i = request.POST.get('intensity')
        r = request.POST.get('resistance')
        print('Intensity =', i)
        print('Resistance =', r)

        try:
            power = float(i) ** 2 * float(r)
            context['p'] = power
        except:
            context['p'] = "Invalid input"

        context['i'] = i
        context['r'] = r
        print('Power =', context['p'])

    return render(request, 'mathapp/math.html', context)
