from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def headphone_info(request):

    model = request.GET.get('model', '').lower()


    headphones_data = {
        'budslive': {
            'name': 'Samsung Galaxy Buds Live',
            'description': 'True wireless earbuds with ANC (Active Noise Cancelling) and a unique design.',
            'price': '159 USD',
        },
        'airpods': {
            'name': 'Apple AirPods',
            'description': 'Wireless earbuds with seamless integration with Apple devices, great sound quality.',
            'price': '159 USD',
        },
        'sonywh1000xm4': {
            'name': 'Sony WH-1000XM4',
            'description': 'Over-ear wireless noise-canceling headphones, acclaimed for comfort and sound quality.',
            'price': '348 USD',
        }
    }

    headphone = headphones_data.get(model)

    if headphone:
        return render(request, 'headphone_info.html', {'headphone': headphone})
    else:
        return render(request, 'headphone_info.html', {'error': 'Model not found'})

