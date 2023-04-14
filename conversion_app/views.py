from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def dec_to_bin(request, number=None):
    if request.method == 'POST':
        number = request.POST.get('dec', None)
        if number is not None:
            binary_number = format(int(number), 'b')
            return render(request, 'dec_to_bin_form.html', {'bin_number': binary_number})
        else:
            return JsonResponse({"error": "No decimal value provided"}, status=400)
    elif number is not None:
        binary_number = format(number, 'b')
        return JsonResponse(binary_number, safe=False)
    else:
        return render(request, 'dec_to_bin_form.html')


@api_view(['GET', 'POST'])
def hex_to_dec(request):
    if request.method == 'POST':
        hex_number = request.POST.get('hex', None)
        if hex_number is not None:
            decimal_number = int(hex_number, 16)
            return render(request, 'hex_to_dec_form.html', {'dec_number': decimal_number})
        else:
            return JsonResponse({"error": "No hex value provided"}, status=400)
    else:
        return render(request, 'hex_to_dec_form.html')
