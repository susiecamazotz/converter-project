from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def dec_to_bin(request, number):
    binary_number = format(number, 'b')
    return JsonResponse(binary_number, safe=False)


@api_view(['POST'])
def hex_to_dec(request):
    hex_number = request.data.get('hex', None)
    if hex_number is not None:
        decimal_number = int(hex_number, 16)
        return JsonResponse({"dec": decimal_number})
    else:
        return JsonResponse({"error": "No hex value provided"}, status=400)
